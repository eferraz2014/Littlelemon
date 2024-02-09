from django.contrib import admin
from .models import BookingTable, Menu, MenuTableSelection
# Register your models here.
admin.site.register(BookingTable)
admin.site.register(Menu)
admin.site.register(MenuTableSelection)