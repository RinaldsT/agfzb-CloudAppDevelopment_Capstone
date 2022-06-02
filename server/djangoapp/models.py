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


# <HINT> Create a plain Python class `DealerReview` to hold review data
