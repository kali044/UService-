from django.contrib import admin
#Register your models here.

from .models import Profile,Textbook_Trading,Carpool,Activity, Tutor

# admin.site.register(Profile)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'rating', 'review')
    fields = ['last_name', 'first_name', 'email', 'rating', 'review']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)


@admin.register(Textbook_Trading)
class TextbookAdmin(admin.ModelAdmin):
    list_display=('title','author','cost','creator')
    fields=['title','author','cost','creator']

@admin.register(Carpool)
class CarpoolAdmin(admin.ModelAdmin):
	list_display = ('creator', 'title', 'destination', 'date', 'cost')
	fields = ['creator', 'title', 'destination', 'date', 'cost']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title','creator','date', 'activity')
	fields = ['title','creator','date', 'activity']

@admin.register(Tutor)
class TutorAdmin (admin.ModelAdmin):
    list_display = ('title', 'creator', 'date', 'cost', 'subject')
    fields = ['title', 'creator', 'date', 'cost', 'subject', 'description']
