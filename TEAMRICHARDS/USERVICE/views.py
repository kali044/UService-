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

    tuName = Tutor.objects.all()[:1].get().creator
    tuType = "Tutor"
    tuSubject = Tutor.objects.all()[:1].get().subject
    tuCost = Tutor.objects.all()[:1].get().cost
    tuDate = Tutor.objects.all()[:1].get().date

    aName = Activity.objects.all()[:1].get().creator
    aType = "Activity"
    aAct = Activity.objects.all()[:1].get().activity
    aDate = Activity.objects.all()[:1].get().date

    return render(
        request,
        'home.html',
        context={'cName': cName, 'cType': cType, "cDestin": cDestin, "cCost": cCost, "cDate": cDate,
        'tName': tName, 'tType':tType, 'tTitle':tTitle, 'tAuthor':tAuthor, 'tCost':tCost, 'tDate':tDate,
        'tuName': tuName, 'tuType': tuType, 'tuSubject': tuSubject, 'tuCost':tuCost,'tuDate':tuDate,
        'aName': aName, 'aType': aType, 'aAct': aAct, 'aDate': aDate},
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
    date = Carpool.objects.all().get().date
    return render(
        request,
        'edit.html',
        context={'date': date}
    )

class carpoolDetailView(generic.DetailView):
    model=Carpool
    context_object_name="carpool"
    template_name='displayTemplate/carpoolDetail.html'

class tutorDetailView(generic.DetailView):
    model=Tutor
    context_object_name="tutor"
    template_name='displayTemplate/tutorDetail.html'

class textbookDetailView(generic.DetailView):
    model=Textbook_Trading
    context_object_name="book"
    template_name='displayTemplate/textbookDetail.html'

class activityDetailView(generic.DetailView):
    model=Activity
    context_object_name="activity"
    template_name='displayTemplate/activityDetail.html'

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



def searchrequest(request):
	return render(
        request,
        'searchRequest.html',
    )

class OfferListView(generic.ListView):
    context_object_name = "offerlist"
    template_name = 'searchOffer.html'
    queryset = Textbook_Trading.objects.all()
    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['books'] = Textbook_Trading.objects.all()
        context['carpools'] = Carpool.objects.all()
        context['tutors'] = Tutor.objects.all()
        context['activitys'] = Activity.objects.all()
        # And so on for more models
        return context
