from rest_framework import serializers
from .models import Menu, BookingTable, MenuTableSelection


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
    def validate(self, data):
        """Check that the number of MenuTableSelection instances is not more than table_selection.nr_of_guests."""
        
        table_selection = data['table_selection']
        selections=MenuTableSelection.objects.filter(table_selection=table_selection)
        sum=sum(selection.number_of_items for selection in selections)
        if sum >= table_selection.nr_of_guests:
            raise serializers.ValidationError("The number of selections is more than the number of guests.")
        return data
