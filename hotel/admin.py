from django.contrib import admin
from .models import Hotel, HotelBooking

#hotel display
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'rating', 'stars', 'category')
    search_fields = ('name', 'city', 'country')
    list_filter = ('stars', 'category', 'city', 'country')
    
#hotel booking display
@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'order_number', 'check_in', 'check_out', 'total_amount')
    search_fields = ('hotel__name', 'order_number')
    list_filter = ('check_in', 'check_out')
