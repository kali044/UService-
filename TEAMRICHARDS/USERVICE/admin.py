from django.contrib import admin
#Register your models here.

from .models import Profile,Textbook_Trading

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
