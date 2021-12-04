from django.db import models
from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model 
class CarMake(models.Model):
    # - Name
    name = models.CharField(max_length=200, default="add name here")
    # - Description
    description = models.CharField(max_length=200, default="add description here")
    # - Any other fields you would like to include in car make model
    # - __str__ method to print a car make object
    def __str__ (self):
        return 'name: ' + self.name + ' \nDescription: ' + self.description


# <HINT> Create a Car Model model 
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # - Name
    name = models.CharField(max_length=200, default="add name here")
    # - Dealer id, used to refer a dealer created in cloudant database
    Dealer_id = models.IntegerField(default=0)
    # - Type CharField with a choices argument to provide limited choices such as
    """class Type_of_car(models.TextChoices):
       SEDAN = 'sd' , 'Sedan'
       SUV = 'sv' , 'SUV'
       WAGON = 'wg' , 'Wagon'
       PICKUP = 'pt' , 'Pickup Truck'
       MINIVAN = 'mv' , 'Minivan'
       CONVERTIBLE = 'cv' , 'Convertible'
       HATCHBACK = 'hb' , 'Hatchback'
       COUPE = 'cp' , 'Coupe'
       SPORTS = 'sc' , 'Sports Car'"""
    
    #carType =  models.CharField(max_length=2, choices = Type_of_car.choices, default=Type_of_car.SEDAN)
    # - Year (DateField)
    year = models.DateField(null=True, default = now)
    # - Any other fields you would like to include in car model
    
    # - __str__ method to print a car make object
    def __str__ (self):
        return f"Manufacturer: {self.maker}\nName: {self.name}\nDealer: {self.Dealer_id}\nType: {self.carType}\nYear: {self.year}" 

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
