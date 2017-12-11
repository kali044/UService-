from django.db import models
from decimal import Decimal
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

class Profile(models.Model):
    """
    Model representing a profile.
    """
    #first_name = models.CharField(max_length=100, help_text="First Name")
    #last_name = models.CharField(max_length=100, help_text="Last Name")
    #email = models.CharField(max_length=100, help_text="johnorjane_doe@email.com")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio=models.TextField(max_length=500,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list                            error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('profile', args=[str(self.id)])

    def edit_url(self):
        return reverse('profile-Edit', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.user)




class Activity(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200, help_text="Enter a Title")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    date = models.DateField(null=True, blank=True)
    activity = models.CharField(max_length=200, help_text="Enter an activity")
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)


    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('activity-Detail', args=[str(self.id)])

    def edit_url(self):
        return reverse('activity-Edit', args=[str(self.id)])

    def create_url(self):
        return reverse('activity-Create', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return  self.title
class Carpool(models.Model):
    """
    Model representing a carpool.
    """
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief desciption of the service")
    destination = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)


    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('carpool-Detail', args=[str(self.id)])

    def edit_url(self):
        return reverse('carpool-Edit', args=[str(self.id)])

    def create_url(self):
        return reverse('carpool-Create', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return  self.title

class Tutor(models.Model):
    """
    Model representing a tutor service
    """
    title = models.CharField(max_length=200, help_text="Enter a tutor service title" )
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text = "Enter a brief description of the tutor")
    date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Enter the of each tutor session")
    subject = models.TextField(max_length=100, help_text="Enter the subject")
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutor-Detail', args=[str(self.id)])

    def edit_url(self):
        return reverse('tutor-Edit', args=[str(self.id)])

    def create_url(self):
        return reverse('tutor-Create', args=[str(self.id)])



class Textbook_Trading(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    creator=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateField(null=True,blank=True)
    cost=models.DecimalField(max_digits=6,decimal_places=2,default=Decimal('0.00'))
    request=models.BooleanField(default=False)
    offer=models.BooleanField(default=False)
    # Metadata

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('textbook-Detail', args=[str(self.id)])

    def edit_url(self):
        return reverse('textbook-Edit', args=[str(self.id)])

    def create_url(self):
        return reverse('textbook-Create', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """

        return self.title

class TutorComment(models.Model):
    post = models.ForeignKey(Tutor, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=200,blank=True,default='')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text


class TextbookComment(models.Model):
    post = models.ForeignKey(Textbook_Trading, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=200,blank=True,default='')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

class CarpoolComment(models.Model):
    post = models.ForeignKey(Carpool, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=200,blank=True,default='')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

class ActivityComment(models.Model):
    post = models.ForeignKey(Activity, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=200,blank=True,default='')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

class PasswordReset(models.Model):
    email = models.CharField(max_length=100)
