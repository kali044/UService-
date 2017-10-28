from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Profile(models.Model):
    """
    Model representing a profile.
    """
    first_name = models.CharField(max_length=100, help_text="First Name")
    last_name = models.CharField(max_length=100, help_text="Last Name")
    email = models.CharField(max_length=100, help_text="johnorjane_doe@email.com")
    review = models.CharField(max_length=500, help_text="Review")

    RATING = (
        ('vb', 'Very Bad'),
        ('b', 'Bad'),
        ('g', 'Good'),
        ('vg', 'Very Good'),
    )

    rating = models.CharField(max_length=1, choices=RATING, blank=True, default='vb', help_text='Rate Me')

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('profile-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

    #not sure if this works
    def edit_profile(newfirstname, newlastname, newemail):
        # Create a new record using the model's constructor.
        firstname = Profile(first_name = newfirstname)
        lastname = Profile(last_name = newlastname)
        email = Profile(first_name = newemail)
        # Save the object into the database.
        firstname.save()
        lastname.save()
        email.save()
        return
