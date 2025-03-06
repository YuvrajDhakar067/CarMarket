from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import Car, CarImage, Transaction, Notification
from .forms import CarForm, CarImageForm, TransactionForm, CarSearchForm

def car_list(request):
    form = CarSearchForm(request.GET)
    cars = Car.objects.filter(is_sold=False)
    
    if form.is_valid():
        search = form.cleaned_data.get('search')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        condition = form.cleaned_data.get('condition')
        location = form.cleaned_data.get('location')
        min_year = form.cleaned_data.get('min_year')
        max_year = form.cleaned_data.get('max_year')
        
        if search:
            cars = cars.filter(
                Q(brand__icontains=search) | 
                Q(model__icontains=search) | 
                Q(description__icontains=search)
            )
        
        if min_price:
            cars = cars.filter(price__gte=min_price)
        
        if max_price:
            cars = cars.filter(price__lte=max_price)
        
        if condition:
            cars = cars.filter(condition=condition)
        
        if location:
            cars = cars.filter(location__icontains=location)
        
        if min_year:
            cars = cars.filter(year__gte=min_year)
        
        if max_year:
            cars = cars.filter(year__lte=max_year)
    
    return render(request, 'cars/car_list.html', {'cars': cars, 'form': form})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def sell_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        image_form = CarImageForm(request.POST, request.FILES)
        
        if car_form.is_valid():
            car = car_form.save(commit=False)
            car.seller = request.user
            car.save()
            
            # Handle multiple images
            images = request.FILES.getlist('image')
            for image in images:
                CarImage.objects.create(car=car, image=image)
            
            # Send email notification
            send_mail(
                'Car Listed Successfully',
                f'Your car {car.brand} {car.model} has been successfully listed for sale!',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            
            messages.success(request, 'Your car has been listed successfully!')
            return redirect('dashboard')
    else:
        car_form = CarForm()
        image_form = CarImageForm()
    
    return render(request, 'cars/sell_car.html', {'car_form': car_form, 'image_form': image_form})

@login_required
def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk, seller=request.user)
    
    if request.method == 'POST':
        car_form = CarForm(request.POST, instance=car)
        
        if car_form.is_valid():
            car_form.save()
            
            # Handle images
            images = request.FILES.getlist('image')
            for image in images:
                CarImage.objects.create(car=car, image=image)
            
            messages.success(request, 'Your car listing has been updated successfully!')
            return redirect('my_listings')
    else:
        car_form = CarForm(instance=car)
        image_form = CarImageForm()
    
    return render(request, 'cars/edit_car.html', {'car_form': car_form, 'image_form': image_form, 'car': car})

@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk, seller=request.user)
    
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Your car listing has been deleted successfully!')
        return redirect('my_listings')
    
    return render(request, 'cars/delete_car.html', {'car': car})

@login_required
def reserve_car(request, pk):
    car = get_object_or_404(Car, pk=pk, is_sold=False)
    
    if car.seller == request.user:
        messages.error(request, 'You cannot reserve your own car!')
        return redirect('car_detail', pk=pk)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST, request.FILES)
        
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.car = car
            transaction.buyer = request.user
            transaction.amount = car.price
            transaction.save()
            
            # Create notification for seller
            Notification.objects.create(
                user=car.seller,
                message=f'New payment request for your {car.brand} {car.model} from {request.user.username}. Please verify the payment details.'
            )
            
            messages.success(request, 'Your payment details have been submitted. The seller will verify and approve your payment.')
            return redirect('dashboard')
    else:
        form = TransactionForm()
    
    return render(request, 'cars/reserve_car.html', {'car': car, 'form': form})

@login_required
def my_listings(request):
    cars = Car.objects.filter(seller=request.user)
    return render(request, 'cars/my_listings.html', {'cars': cars})

@login_required
def my_purchases(request):
    transactions = Transaction.objects.filter(buyer=request.user)
    return render(request, 'cars/my_purchases.html', {'transactions': transactions})

@login_required
def payment_requests(request):
    transactions = Transaction.objects.filter(car__seller=request.user, status='Pending')
    return render(request, 'cars/payment_requests.html', {'transactions': transactions})

@login_required
def approve_payment(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, car__seller=request.user)
    
    if request.method == 'POST':
        transaction.status = 'Approved'
        transaction.save()
        
        # Update car status
        car = transaction.car
        car.is_sold = True
        car.save()
        
        # Create notification for buyer
        Notification.objects.create(
            user=transaction.buyer,
            message=f'Your payment for {car.brand} {car.model} has been approved. The car will be delivered to you soon.'
        )
        
        messages.success(request, 'Payment has been approved successfully!')
        return redirect('payment_requests')
    
    return render(request, 'cars/approve_payment.html', {'transaction': transaction})

@login_required
def reject_payment(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, car__seller=request.user)
    
    if request.method == 'POST':
        transaction.status = 'Rejected'
        transaction.save()
        
        # Create notification for buyer
        Notification.objects.create(
            user=transaction.buyer,
            message=f'Your payment for {transaction.car.brand} {transaction.car.model} has been rejected. Please re-upload correct payment details.'
        )
        
        messages.success(request, 'Payment has been rejected successfully!')
        return redirect('payment_requests')
    
    return render(request, 'cars/reject_payment.html', {'transaction': transaction})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    # Mark all as read
    unread_notifications = notifications.filter(is_read=False)
    unread_notifications.update(is_read=True)
    
    return render(request, 'cars/notifications.html', {'notifications': notifications})
