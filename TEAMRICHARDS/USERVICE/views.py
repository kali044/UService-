from django.shortcuts import render
from django.views import generic

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
        'index.html',
        context={'num_users':num_users,'num_profile':num_profile,
        'num_activities':num_activities,'num_tutor':num_tutor, 'num_textbook_trade':num_textbook_trade},
    )

def home(request):

    cName = Carpool.objects.all()[:1].get().creator
    cType = "Carpool"
    cDestin = Carpool.objects.all()[:1].get().destination
    cCost = Carpool.objects.all()[:1].get().cost
    cDate = Carpool.objects.all()[:1].get().date

    tName = Textbook_Trading.objects.all()[:1].get().creator
    tType = "Textbook Trading"
    tTitle = Textbook_Trading.objects.all()[:1].get().title
    tAuthor = Textbook_Trading.objects.all()[:1].get().author
    tCost = Textbook_Trading.objects.all()[:1].get().cost
    tDate = Textbook_Trading.objects.all()[:1].get().date

    return render(
        request,
        'home.html',
        context={'cName': cName, 'cType': cType, "cDestin": cDestin, "cCost": cCost, "cDate": cDate,
        'tName': tName, 'tType':tType, 'tTitle':tTitle, 'tAuthor':tAuthor, 'tCost':tCost, 'tDate':tDate},
    )

def about(request):
	return render(
        request,
        'about.html',
    )

def addoffer(request):
	return render(
        request,
        'addOffer.html',
    )

def addrequest(request):
	return render(
        request,
        'addRequest.html',
    )

def edit(request):
	return render(
        request,
        'edit.html',
    )

class offerservicedetailView(generic.DetailView):
    model=Carpool
    context_object_name='carpoolDetail'
    template_nam='OfferServiceDetail.html'

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
