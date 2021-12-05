from django.db import models
from django.utils.timezone import now

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=200, default="add name here")
    description = models.CharField(max_length=200, default="add description here")
    def __str__ (self):
        return 'name: ' + self.name + ' \nDescription: ' + self.description


class CarModel(models.Model):
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="add name here")
    Dealer_id = models.IntegerField(default=0)
    class Type_of_car(models.TextChoices):
       SEDAN = 'sd' , 'Sedan'
       SUV = 'sv' , 'SUV'
       WAGON = 'wg' , 'Wagon'
       PICKUP = 'pt' , 'Pickup Truck'
       MINIVAN = 'mv' , 'Minivan'
       CONVERTIBLE = 'cv' , 'Convertible'
       HATCHBACK = 'hb' , 'Hatchback'
       COUPE = 'cp' , 'Coupe'
       SPORTS = 'sc' , 'Sports Car'
    
    carType =  models.CharField(max_length=2, choices = Type_of_car.choices, default=Type_of_car.SEDAN)
    year = models.DateField(null=True, default = now)
    def __str__ (self):
        return f"Manufacturer: {self.maker}\nName: {self.name}\nDealer: {self.Dealer_id}\nType: {self.carType}\nYear: {self.year}" 

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
