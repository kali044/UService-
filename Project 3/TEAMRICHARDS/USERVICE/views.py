from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
import datetime

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
    date = Carpool.objects.all()[:1].get().date
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


def profile(request):

    name = User.objects.all()[:1].get().name
    email = User.objects.all()[:1].get().email
    rating = Profile.objects.all()[:1].get().rating
    rating = dict(Profile.RATING).get(rating)
    review = Profile.objects.all()[:1].get().review

    return render(
        request,
        'profile.html',
        context={'name':name, 'email': email,'rating': rating, 'review':review
        },
    )



class offerListView(generic.ListView):
    context_object_name = "offerlist"
    template_name = 'searchOffer.html'
    queryset = Textbook_Trading.objects.all()
    def get_context_data(self, **kwargs):
        context = super(offerListView, self).get_context_data(**kwargs)
        context['books'] = Textbook_Trading.objects.filter(offer=True)
        context['carpools'] = Carpool.objects.filter(offer=True)
        context['tutors'] = Tutor.objects.filter(offer=True)
        context['activitys'] = Activity.objects.filter(offer=True)
        # And so on for more models
        return context

class requestListView(generic.ListView):
    context_object_name = "requestlist"
    template_name = 'searchRequest.html'
    queryset = Textbook_Trading.objects.all()
    def get_context_data(self, **kwargs):
        context = super(requestListView, self).get_context_data(**kwargs)
        context['books'] = Textbook_Trading.objects.filter(request=True)
        context['carpools'] = Carpool.objects.filter(request=True)
        context['tutors'] = Tutor.objects.filter(request=True)
        context['activitys'] = Activity.objects.filter(request=True)
        # And so on for more models
        return context


class mypublishListView(generic.ListView):
    context_object_name = "mypublishlist"
    template_name = 'mypublish.html'
    queryset = Textbook_Trading.objects.all()
    def get_context_data(self, **kwargs):
        context = super(mypublishListView, self).get_context_data(**kwargs)
        context['books'] = Textbook_Trading.objects.all()
        context['carpools'] = Carpool.objects.all()
        context['tutors'] = Tutor.objects.all()
        context['activitys'] = Activity.objects.all()
        
        # context['books'] = Textbook_Trading.objects.filter(creator=self.request.user)
        # context['carpools'] = Carpool.objects.filter(creator=self.request.user)
        # context['tutors'] = Tutor.objects.filter(creator=self.request.user)
        # context['activitys'] = Activity.objects.filter(creator=self.request.user)
        # And so on for more models
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activity, Tutor, Carpool, Textbook_Trading

class ActivityCreate(CreateView):
    model = Activity
    fields = '__all__'
    initial={'title':'A fun Activity',}

class ActivityUpdate(UpdateView):
    model = Activity
    context_object_name='activity'
    fields = ['title','description','date','activity']
    template_name='edit.html'

class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('/home') #{% static 'templates/profile' %}??

class CarpoolCreate(CreateView):
    model = Carpool
    fields = '__all__'
    initial={'title':'Riding is better not alone!',}

class CarpoolUpdate(UpdateView):
    model = Carpool
    context_object_name='carpool'
    fields = ['title','description','destination','date','cost']
    template_name='edit.html'

class CarpoolDelete(DeleteView):
    model = Carpool
    success_url = reverse_lazy('/home')

class TutorCreate(CreateView):
    model = Tutor
    fields = '__all__'
    initial={'title':'Teaching is fun!',}

class TutorUpdate(UpdateView):
    model = Tutor
    context_object_name='Tutor'
    fields = ['title','description','date','cost','subject']
    template_name='edit.html'

class TutorDelete(DeleteView):
    model = Tutor
    success_url = reverse_lazy('/home')

class Textbook_TradingCreate(CreateView):
    model = Textbook_Trading
    fields = '__all__'
    initial={'title':'I want or need a book!',}

class Textbook_TradingUpdate(UpdateView):
    model = Textbook_Trading
    context_object_name='textbook_trading'
    fields = ['title','author','description','date','cost']
    template_name='edit.html'

class Textbook_TradingDelete(DeleteView):
    model = Textbook_Trading
    success_url = reverse_lazy('/home')


