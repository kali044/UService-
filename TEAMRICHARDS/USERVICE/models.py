from django.db import models

# Create your models here.
<<<<<<< HEAD
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
    	title.save()
    	return 

    def modifyDescription(self,desc2):
    	self.description = desc2
    	description.save()
    	return

    def modifyDate(self,date2):
    	self.date = date2
    	date.save()
    	return

    def modifyActivity(self,act2):
    	self.activity = act2
    	activity.save()
    	return
    	    
=======
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

