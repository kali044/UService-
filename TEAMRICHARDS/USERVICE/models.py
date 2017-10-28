from django.db import models
from decimal import Decimal

# Create your models here.

class Carpool(models.Model):
    """
    Model representing a carpool.
    """
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief desciption of the service")
    destination = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    def edit_title(self, new_title):
        """
        Edit title for the Carpool.
        """
        self.title = new_title

    def edit_description(self, new_desciption):
        """
        Edit desciption for the Carpool.
        """
        self.desciption = new_desciption

    def edit_destination(self, new_destination):
        """
        Edit destination for the Carpool.
        """
        self.destination = new_destination

    def edit_date(self, new_date):
        """
        Edit date for the Carpool.
        """
        self.date = new_date

    def edit_cost(self, new_cost):
        """
        Edit cost for the Carpool.
        """
        self.cost = new_cost
