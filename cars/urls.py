from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('sell/', views.sell_car, name='sell_car'),
    path('edit/<int:pk>/', views.edit_car, name='edit_car'),
    path('delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('reserve/<int:pk>/', views.reserve_car, name='reserve_car'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('my-purchases/', views.my_purchases, name='my_purchases'),
    path('payment-requests/', views.payment_requests, name='payment_requests'),
    path('approve-payment/<int:pk>/', views.approve_payment, name='approve_payment'),
    path('reject-payment/<int:pk>/', views.reject_payment, name='reject_payment'),
    path('notifications/', views.notifications, name='notifications'),
] 