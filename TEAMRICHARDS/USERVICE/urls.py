from django.conf.urls import url
from django.views import generic

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^addoffer/', views.addoffer, name='addoffer'),
    url(r'^addrequest/', views.addrequest, name='addrequest'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^carpoolDetail/(?P<pk>\d+)$', views.carpoolDetailView.as_view(), name='carpool-Detail'),
    url(r'^tutorDetail/(?P<pk>\d+)$', views.tutorDetailView.as_view(), name='tutor-Detail'),
    url(r'^textbookDetail/(?P<pk>\d+)$', views.textbookDetailView.as_view(), name='textbook-Detail'),
    url(r'^activityDetail/(?P<pk>\d+)$', views.activityDetailView.as_view(), name='activity-Detail'),
    url(r'^requestservicedetail/', views.requestservicedetail, name='requestservicedetail'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^searchoffer/$', views.offerListView.as_view(), name='searchoffer'),
    url(r'^searchrequest/$', views.requestListView.as_view(), name='searchrequest'),


]
