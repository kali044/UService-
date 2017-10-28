from django.contrib import admin

#Register your models here.

from .models import Profile, Activity, Carpool, Tutor, Textbook_Trading


# admin.site.register(Profile)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'rating', 'review')
    fields = ['last_name', 'first_name', 'email', 'rating', 'review']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title','creator','date', 'activity')
	fields = ['title','creator','date', 'activity']


@admin.register(Carpool) 
class CarpoolAdmin(admin.ModelAdmin):
	list_display = ('creator', 'title', 'destination', 'date', 'cost')
	fields = ['creator', 'title', 'destination', 'date', 'cost']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

