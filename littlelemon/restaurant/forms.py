from django.forms import ModelForm
from .models import BookingTable, Menu, MenuTableSelection,UserModel
# Create your forms here.


class UserModelForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class LoginForm(ModelForm):
    class Meta:
        model = UserModel
        fields = {'username', 'password'}

class BookingTableForm(ModelForm):
    class Meta:
        model = BookingTable
        fields = "__all__"


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuTableSelectionForm(ModelForm):
    class Meta:
        model = MenuTableSelection
        fields = "__all__"
