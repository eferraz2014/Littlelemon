from django.contrib import admin
from .models import Booking, MenuItem , MenuSelection,UserModel
# Register your models here.
admin.site.register(Booking)
admin.site.register(MenuItem )
admin.site.register(MenuSelection)
admin.site.register(UserModel)