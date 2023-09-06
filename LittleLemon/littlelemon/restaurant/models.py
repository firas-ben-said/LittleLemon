from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return f'{self.name} : {str(self.price)}'
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    num = models.IntegerField()
    def __str__(self):
        return self.name