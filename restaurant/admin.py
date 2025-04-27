from django.contrib import admin
from .models import Dish, Reservation

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'number_of_people')
    list_filter = ('date',)
    search_fields = ('user__username', 'special_request')
