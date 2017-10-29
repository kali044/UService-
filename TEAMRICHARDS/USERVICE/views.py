from django.shortcuts import render

# Create your views here.

from .models import User, Profile, Textbook_Trading, Carpool, Activity, Tutor

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_users=User.objects.all().count()
    num_profile=Profile.objects.all().count()
    num_activities=Activity.objects.all().count()
    num_tutor=Tutor.objects.all().count()
    num_textbook_trade=Textbook_Trading.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_users':num_users,'num_profile':num_profile,
        'num_activities':num_activities,'num_tutor':num_tutor, 'num_textbook_trade':num_textbook_trade},
    )

def home(request):
	return render(
        request,
        'home.html',
    )

def about(request):
	return render(
        request,
        'about.html',
    )

def addoffer(request):
	return render(
        request,
        'addoffer.html',
    )

def addrequest(request):
	return render(
        request,
        'addrequest.html',
    )

def edit(request):
	return render(
        request,
        'edit.html',
    )

def offerservicedetail(request):
	return render(
        request,
        'OfferServiceDetail.html',
    )

def requestservicedetail(request):
	return render(
        request,
        'RequestServiceDetail.html',
    )

def profile(request):
	return render(
        request,
        'profile.html',
    )

def searchoffer(request):
	return render(
        request,
        'searchOffer.html',
    )

def searchrequest(request):
	return render(
        request,
        'searchRequest.html',
    )
