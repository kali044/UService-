from django.contrib import admin

#Register your models here.

from .models import Profile

# admin.site.register(Profile)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'rating', 'review')
    fields = ['last_name', 'first_name', 'email', 'rating', 'review']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)
