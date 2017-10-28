from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Carpool(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

# class Profile(models.Model):
#     """
#     Model representing an author.
#     """
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     rating = models.CharField(max_length=100)
#     review = models.CharField(max_length=100)
#
#     def get_absolute_url(self):
#         """
#         Returns the url to access a particular author instance.
#         """
#         return reverse('profile-detail', args=[str(self.id)])
#
#
#     def __str__(self):
#         """
#         String for representing the Model object.
#         """
#         return '%s, %s' % (self.last_name, self.first_name)
