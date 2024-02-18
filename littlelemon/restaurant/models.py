from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class UserModel(User):
    class Meta:
        proxy = True
    def __str__(self):
         return self.username

class BookingTable(models.Model):
    name = models.CharField(max_length=100)
    nr_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name + ' - ' + str(self.booking_date.strftime('%d/%m/%Y - %H:%M:%S'))

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    def __str__(self):
        return self.title

class MenuTableSelection(models.Model):
    table_selection = models.ForeignKey(BookingTable, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Menu, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.table_selection.name