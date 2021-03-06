from django.db import models
from decimal import Decimal
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, help_text="Name")
    email = models.CharField(max_length=100, help_text="Email")
    password = models.CharField(max_length=10, help_text="Password")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('user-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.name, self.email)

    

class Profile(models.Model):
    """
    Model representing a profile.
    """
    #first_name = models.CharField(max_length=100, help_text="First Name")
    #last_name = models.CharField(max_length=100, help_text="Last Name")
    #email = models.CharField(max_length=100, help_text="johnorjane_doe@email.com")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
        return '%s' % (self.user)

    #not sure if this works
    def edit_profile(self, new_user):
        # Create a new record using the model's constructor.
        self.user = new_user
        # Save the object into the database.
        self.user.save()
        return


class Activity(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200, help_text="Enter a Title")
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    date = models.DateField(null=True, blank=True)
    activity = models.CharField(max_length=200, help_text="Enter an activity")
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    def modifyTitle(self, title2):
        self.title = title2

    def modifyDescription(self,desc2):
        self.description = desc2


    def modifyDate(self,date2):
        self.date = date2


    def modifyActivity(self,act2):
        self.activity = act2

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('activity-Detail', args=[str(self.id)])

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

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('carpool-Detail', args=[str(self.id)])

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
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text = "Enter a brief description of the tutor")
    date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Enter the of each tutor session")
    subject = models.TextField(max_length=100, help_text="Enter the subject")
    request = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    def editTitle(newTitle, self):
        if (newTitle!=None):
            self.title = newTitle

    def editDescription(newDesc, self):
        if (newDesc != None):
            self.description = newDesc

    def editDate(newDate, self):
        if (newDate != None):
            self.date = newDate

    def editCost(newCost, self):
        if (newCost != None):
            self.cost = newCost

    def editSubject(newSubject, self):
        if (newSubject != None):
            self.subject = newSubject

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutor-Detail', args=[str(self.id)])


class Textbook_Trading(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    creator=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    date=models.DateField(null=True,blank=True)
    cost=models.DecimalField(max_digits=4,decimal_places=2,default=Decimal('0.00'))
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
         return reverse('textbook-Detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """

        return self.title
