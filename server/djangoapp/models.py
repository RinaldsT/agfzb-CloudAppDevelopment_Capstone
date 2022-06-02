from django.db import models
from django.utils.timezone import now


# Create your models here.
TYPE_CHOICES = (
    ("SEDAN", "Sedan"),
    ("SUV", "SUV"),
    ("WAGON", "WAGON"),
)

class CarMake(models.Model):
    Name = models.CharField('Car maker', max_length = 50)
    Description = models.TextField('Description', max_length = 200)
    
    def __str__(self):
        return self.Name

class CarModel(models.Model):
    Model = models.ForeignKey(CarMake, on_delete = models.CASCADE)
    Name = models.CharField('Car model', max_length = 50)
    Dealer_Id = models.IntegerField('Dealer ID in cloudant DB')
    Type = models.CharField(max_length = 20, choices = TYPE_CHOICES, default = 'SEDAN')
    Year = models.DateField(default=now)
    
    def __str__(self):
        return self.Name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.state = state
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return self.review