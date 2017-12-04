from django.contrib import admin
from django.contrib.auth.models import User
#Register your models here.

from .models import Profile, Textbook_Trading, Carpool, Activity, Tutor, TutorComment, TextbookComment, CarpoolComment, ActivityComment

# admin.site.register(Profile)

# class UserAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'email', 'password')
# 	fields = ['name', 'email', 'password']

# Register the admin class with the associated model
# admin.site.register(User, UserAdmin)

# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'review')
    fields = ['user', 'rating', 'review']

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)


@admin.register(Textbook_Trading)
class TextbookAdmin(admin.ModelAdmin):
    list_display=('title','author','cost', 'date','creator','request','offer')
    fields=['title','author','description','date','cost','creator','request','offer']

@admin.register(Carpool)
class CarpoolAdmin(admin.ModelAdmin):
	list_display = ('creator', 'title', 'destination', 'date', 'cost','request','offer')
	fields = ['creator', 'title', 'destination', 'description', 'date', 'cost','request','offer']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title','creator','date', 'activity','request','offer')
	fields = ['title','creator','date','activity', 'description','request','offer']


@admin.register(Tutor)
class TutorAdmin (admin.ModelAdmin):
    list_display = ('title', 'creator', 'date', 'cost', 'subject','request','offer')
    fields = ['title', 'creator', 'date', 'cost', 'subject', 'description','request','offer']
admin.site.register(TutorComment)
admin.site.register(TextbookComment)
admin.site.register(CarpoolComment)
admin.site.register(ActivityComment)
