from django.contrib import admin

# Register your models here.

from .models import Service, Profile


# Define the admin class
@admin.register(Profile)
class ProfileAdmin(admin.ModelProfile):
    list_display = ('last_name', 'first_name', 'email', 'rating', 'review')
    fields = ['first_name', 'last_name', 'email', 'rating', 'review']

admin.site.register(Profile, ProfileAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Service)
class Service(admin.ModelService):
    list_display = ('title')
