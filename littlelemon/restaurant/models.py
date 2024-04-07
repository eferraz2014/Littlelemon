from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class UserModel(User):
    class Meta:
        proxy = True
    def __str__(self):
         return self.username

class MenuItem(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    nr_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField(default=datetime.now, blank=False)
    menuitems = models.ManyToManyField('MenuItem', through='MenuSelection', related_name='menuitems', blank=True)
    def __str__(self):
        return self.name + ' - ' + str(self.booking_date.strftime('%d/%m/%Y - %H:%M:%S'))
    class Meta:
        ordering = ["booking_date","name"]

class MenuSelection(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,blank=True, null=True)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, blank=True, null=True)
    number_of_items = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        if self.booking:
            return self.booking.name+' - '+self.booking.booking_date.strftime('%d/%m/%Y - %H:%M:%S')
        return 'No Booking'
