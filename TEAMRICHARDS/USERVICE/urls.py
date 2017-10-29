from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^addoffer/', views.addoffer, name='addoffer'),
    url(r'^addrequest/', views.addrequest, name='addrequest'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^offerservicedetail/', views.offerservicedetail, name='offerservicedetail'),
    url(r'^requestservicedetail/', views.requestservicedetail, name='requestservicedetail'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^searchoffer/', views.searchoffer, name='searchoffer'),
    url(r'^searchrequest/', views.searchrequest, name='searchrequest'),
]
