from django.db import models

# Create your models here.
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
    	    
