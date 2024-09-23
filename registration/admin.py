from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    list_filter = ['returned_on', 'took_on']
    list_display = ('last_name', 'first_name', 'cost', 'returned_on')
















