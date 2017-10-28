from django.contrib import admin
#Register your models here.

from .models import User, Profile, Textbook_Trading, Carpool, Activity, Tutor

# admin.site.register(Profile)

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'password')
	fields = ['name', 'email', 'password']

# Register the admin class with the associated model
admin.site.register(User, UserAdmin)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'review')
    fields = ['user', 'rating', 'review']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)


@admin.register(Textbook_Trading)
class TextbookAdmin(admin.ModelAdmin):
    list_display=('title','author','cost','creator')
    fields=['title','author','description','cost','creator']

@admin.register(Carpool)
class CarpoolAdmin(admin.ModelAdmin):
	list_display = ('creator', 'title', 'destination', 'date', 'cost')
	fields = ['creator', 'title', 'destination', 'description', 'date', 'cost']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title','creator','date', 'activity')
	fields = ['title','creator', 'description', 'date', 'activity']

@admin.register(Tutor)
class Tutor (admin.ModelAdmin):
    list_display = ('title', 'creator', 'date', 'cost', 'subject')
    fields = ['title', 'creator', 'date', 'cost', 'subject', 'description']
