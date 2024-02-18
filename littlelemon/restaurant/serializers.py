from rest_framework import serializers
from .models import Menu, BookingTable, MenuTableSelection,UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = {'username', 'password', 'email', 'first_name', 'last_name'}
        
class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuTableSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTableSelection
        fields = '__all__'        
