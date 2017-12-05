from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
import datetime
from django.apps import apps
# Create your views here.

from .forms import TextbookCommentForm, TutorCommentForm, ActivityCommentForm, CarpoolCommentForm
from .models import Profile, Textbook_Trading, Carpool, Activity, Tutor,  TutorComment, TextbookComment, CarpoolComment, ActivityComment
from django.shortcuts import redirect
# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_users=User.objects.all().count()
#     num_profile=Profile.objects.all().count()
#     num_activities=Activity.objects.all().count()
#     num_tutor=Tutor.objects.all().count()
#     num_textbook_trade=Textbook_Trading.objects.all().count()
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'index.html',
#         context={'num_users':num_users,'num_profile':num_profile,
#         'num_activities':num_activities,'num_tutor':num_tutor, 'num_textbook_trade':num_textbook_trade},
#     )

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

from django.contrib.auth.decorators import login_required
@login_required
def profile(request):

    name = User.objects.all()[:1].get().username
    email = User.objects.all()[:1].get().email

    rating = Profile.objects.filter(user=request.user).get().rating
    rating = dict(Profile.RATING).get(rating)
    review = Profile.objects.filter(user=request.user).get().review

    return render(
        request,
        'profile.html',
        context={'name':name, 'email': email,'rating': rating, 'review':review
        },
    )


class offerListView(generic.ListView):
    context_object_name = "offerlist"
    template_name = 'searchOffer.html'
   
    def get_queryset(self):
        if self.request.method == 'GET':
            model = Textbook_Trading
            modelfields = self.request.GET.get('modelfields',None)
            search_query = self.request.GET.get('q',None)
            if modelfields:
                model = apps.get_model('USERVICE',modelfields)
            if search_query and modelfields:
                return model.objects.filter(offer=True).filter(title__icontains = search_query)
            else:
                return model.objects.filter(offer=True)
    

class requestListView(generic.ListView):
    context_object_name = "requestlist"
    template_name = 'searchRequest.html'
   
    def get_queryset(self):
        if self.request.method == 'GET':
            model = Textbook_Trading
            modelfields = self.request.GET.get('modelfields',None)
            search_query = self.request.GET.get('q',None)
            if modelfields:
                model = apps.get_model('USERVICE',modelfields)
            if search_query and modelfields:
                return model.objects.filter(request=True).filter(title__icontains = search_query)
            else:
                return model.objects.filter(request=True)

from django.contrib.auth.mixins import LoginRequiredMixin
class mypublishListView(LoginRequiredMixin,generic.ListView):
    context_object_name = "mypublishlist"
    template_name = 'mypublish.html'
    queryset = Textbook_Trading.objects.all()
    def get_context_data(self, **kwargs):
        context = super(mypublishListView, self).get_context_data(**kwargs)

        context['books'] = Textbook_Trading.objects.filter(creator=self.request.user)
        context['carpools'] = Carpool.objects.filter(creator=self.request.user)
        context['tutors'] = Tutor.objects.filter(creator=self.request.user)
        context['activitys'] = Activity.objects.filter(creator=self.request.user)

        # And so on for more models
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activity, Tutor, Carpool, Textbook_Trading


class ActivityCreateRequest(CreateView):
    model = Activity
    context_object_name='activity'
    fields = ['title','description','date','activity']
    template_name='addRequest2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = True
        form.instance.offer = False
        return super().form_valid(form)

class ActivityCreateOffer(CreateView):
    model = Activity
    context_object_name='activity'
    fields = ['title','description','date','activity']
    template_name='addOffer2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = False
        form.instance.offer = True
        return super().form_valid(form)

class ActivityUpdate(UpdateView):
    model = Activity
    context_object_name='activity'
    fields = ['title','description','date','activity']
    template_name='edit.html'

class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('/home') #{% static 'templates/profile' %}??


class CarpoolCreateRequest(CreateView):
    model = Carpool
    context_object_name='carpool'
    fields = ['title','description','destination','date','cost']
    template_name='addRequest2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = True
        form.instance.offer = False
        return super().form_valid(form)


class CarpoolCreateOffer(CreateView):
    model = Carpool
    context_object_name='carpool'
    fields = ['title','description','destination','date','cost']
    template_name='addOffer2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = False
        form.instance.offer = True
        return super().form_valid(form)

class CarpoolUpdate(UpdateView):
    model = Carpool
    context_object_name='carpool'
    fields = ['title','description','destination','date','cost']
    template_name='edit.html'

class CarpoolDelete(DeleteView):
    model = Carpool
    success_url = reverse_lazy('/home')

class TutorCreateRequest(CreateView):
    model = Tutor
    context_object_name='tutor'
    fields = ['title','description','date','cost','subject']
    template_name='addRequest2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = True
        form.instance.offer = False
        return super().form_valid(form)


class TutorCreateOffer(CreateView):
    model = Tutor
    context_object_name='tutor'
    fields = ['title','description','date','cost','subject']
    template_name='addOffer2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = False
        form.instance.offer = True
        return super().form_valid(form)

class TutorUpdate(UpdateView):
    model = Tutor
    context_object_name='tutor'
    fields = ['title','description','date','cost','subject']
    template_name='edit.html'

class TutorDelete(DeleteView):
    model = Tutor
    success_url = reverse_lazy('/home')


class Textbook_TradingCreateRequest(CreateView):
    model = Textbook_Trading
    context_object_name='textbook_trading'
    fields = ['title','author','description','date','cost']
    template_name='addRequest2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = True
        form.instance.offer = False
        return super().form_valid(form)


class Textbook_TradingCreateOffer(CreateView):
    model = Textbook_Trading
    context_object_name='textbook_trading'
    fields = ['title','author','description','date','cost']
    template_name='addOffer2.html'

    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.request = False
        form.instance.offer = True
        return super().form_valid(form)

class Textbook_TradingUpdate(UpdateView):
    model = Textbook_Trading
    context_object_name='textbook_trading'
    fields = ['title','author','description','date','cost']
    template_name='edit.html'

class Textbook_TradingDelete(DeleteView):
    model = Textbook_Trading
    success_url = reverse_lazy('/home')
@login_required
def add_comment_to_book(request, pk):
    post = get_object_or_404(Textbook_Trading, pk=pk)
    if request.method == "POST":
        form = TextbookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user.username
            comment.save()
            return redirect('textbook-Detail', pk=post.pk)
    else:
        form =TextbookCommentForm()
    return render(request, 'USERVICE/addComment.html', {'form': form})
@login_required
def add_comment_to_carpool(request, pk):
    post = get_object_or_404(Carpool, pk=pk)
    if request.method == "POST":
        form = CarpoolCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user.username
            comment.save()
            return redirect('carpool-Detail', pk=post.pk)
    else:
        form =CarpoolCommentForm()
    return render(request, 'USERVICE/addComment.html', {'form': form})
@login_required
def add_comment_to_tutor(request, pk):
    post = get_object_or_404(Tutor, pk=pk)
    if request.method == "POST":
        form = TutorCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user.username
            comment.save()
            return redirect('tutor-Detail', pk=post.pk)
    else:
        form =TutorCommentForm()
    return render(request, 'USERVICE/addComment.html', {'form': form})
@login_required
def add_comment_to_activity(request, pk):
    post = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user.username
            comment.save()
            return redirect('activity-Detail', pk=post.pk)
    else:
        form =ActivityCommentForm()
    return render(request, 'USERVICE/addComment.html', {'form': form})
