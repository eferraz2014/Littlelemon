from rest_framework import serializers
from .models import MenuItem, Booking, MenuSelection,UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 0},
        }

class BookingSerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = ['name', 'nr_of_guests', 'booking_date', 'menuitems']
        depth=1
  
class MenuSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSelection
        fields = '__all__' 