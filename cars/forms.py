from django import forms
from .models import Car, CarImage, Transaction

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'condition', 'mileage', 'price', 'location', 'description', 'upi_id']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'payment_screenshot']
        widgets = {
            'transaction_id': forms.TextInput(attrs={'placeholder': 'Enter UPI transaction ID'}),
        }

class CarSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search by brand, model...'}))
    min_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Min Price'}))
    max_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Max Price'}))
    condition = forms.ChoiceField(
        required=False,
        choices=[('', 'All Conditions')] + list(Car.CONDITION_CHOICES),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    min_year = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Min Year'}))
    max_year = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Max Year'})) 