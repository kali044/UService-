from django.db import models

# Create your models here.

class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name


class Tutor(models.Model):
    """
    Model representing a tutor service 
    """

    title = models.CharField(max_length=200, help_text="Enter a tutor service title" )
    description = models.TextField(max_length=1000, help_text = "Enter a brief description of the tutor")
    date = model.DateField(null=True, blank=True)
    cost = model.DecmialField(max_digits=6, decimal_places=2, help_text="Enter the of each tutor session")
    subject = model.TextField(max_length=100, help_text="Enter the subject")
    request = model.BooleanField(default=False)
    offer = model.BooleanField(default=False)

    def editTitle(newTitle, self):
        if (newTitle!=NULL)
            self.title = newTitle

    def editDescription(newDesc, self):
        if (newDesc != NULL)
            self.description = newDesc

    def editDate(newDate, self):
        if (newDate != NULL)
            self.date = newDate

    def editCost(newCost, self):
        if (newCost != NULL)
            self.cost = newCost

    def editSubject(newSubject, self):
        if (newSubject != NULL)
            self.subject = newSubject

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutor', args=[str(self.id)])
