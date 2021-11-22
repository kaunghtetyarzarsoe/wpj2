from django.contrib import admin
from .models import Sellrecord

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'price', 'purchased_items', 'showroom', 'paid', 'date']
    list_filter = ['customer_name', 'customer_phone', 'price', 'purchased_items', 'showroom', 'paid', 'date']
    search_field = ['customer_name', 'customer_phone', 'price', 'purchased_items', 'showroom', 'paid', 'date']

admin.site.register(Sellrecord, SellrecordAdmin)