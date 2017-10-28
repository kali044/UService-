from django.contrib import admin
from .models import Textbook_Trading
#Register your models here.

from .models import Profile, Activity, Carpool, Tutor, Textbook_Trading


# admin.site.register(Profile)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'rating', 'review')
    fields = ['last_name', 'first_name', 'email', 'rating', 'review']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

<<<<<<< HEAD
@admin.register(Textbook_Trading)
class TextbookAdmin(admin.ModelAdmin):
    list_display=('title','author','cost','creator')
    fields=['title','author','cost','creator']
    inlines=[TextbookInLine]
class TextbookInLine(admin.TabularInline):
    model = Textbook_Trading
=======
@admin.register(Carpool) 
class CarpoolAdmin(admin.ModelAdmin):
	list_display = ('creator', 'title', 'destination', 'date', 'cost')
	fields = ['creator', 'title', 'destination', 'date', 'cost']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title','creator','date', 'activity')
	fields = ['title','creator','date', 'activity']
>>>>>>> 90f33146bb6e2f0da34ae5e8ff52ecc5c95a28d0
