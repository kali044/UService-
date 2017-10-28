from django.db import models
from decimal import Decimal

# Create your models here.

class Textbook_Trading(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    creator=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    date=models.DateField(null=True,blank=True)
    cost=models.DecimalField(max_digits=4,decimal_places=2,default=Decimal('0,00'))
    request=models.BooleanField(default=False)
    offer=models.BooleanField(default=False)
    # Metadata
    def edit_title(self,newTitle):
        self.title=newTitle
    def edit_author(self,new_Author):
        self.author=new_Author
    def edit_description(self,new_description):
        self.description=new_description
    def edit_creator(self,new_creator):
        self.creator=new_creator
    def edit_data(self,newDate):
        self.date=newDate
    def edit_cost(self,newCost):
        self.cost=newCost

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('Textbook details', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
