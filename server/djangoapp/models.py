from django.db import models
from django.utils.timezone import now

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    # Add any other fields you want for a car make here

    def __str__(self):
        return self.name  # Display the name of the car make as its string representation


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-To-One relationship with CarMake
    dealer_id = models.IntegerField()  # Dealer Id referring to a dealer created in Cloudant database
    name = models.CharField(max_length=100)  # Name of the car model
    TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        # Add other choices as needed
    )
    car_type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Type of the car (limited choices)
    year = models.DateField()  # Year of the car model
    # Add any other fields you want for a car model here

    def __str__(self):
        return self.name  # Display the name of the car model as its string representation


# Plain Python class to hold dealer data
class CarDealer:
    def __init__(self, dealer_id, name, address, city, state, zip):
        self.dealer_id = dealer_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip


# Plain Python class to hold review data
class DealerReview:
    def __init__(self, dealer_id, review_id, review, purchase, purchase_date, car_make, car_model, review_date):
        self.dealer_id = dealer_id
        self.review_id = review_id
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.review_date = review_date


