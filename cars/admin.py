from django.contrib import admin
from .models import Car, CarImage, Transaction, Notification

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'seller', 'is_sold', 'created_at')
    list_filter = ('is_sold', 'condition', 'brand')
    search_fields = ('brand', 'model', 'description')
    inlines = [CarImageInline]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('car', 'buyer', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('car__brand', 'car__model', 'buyer__username')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('user__username', 'message')
