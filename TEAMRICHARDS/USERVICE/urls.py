from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^home/about', views.about, name='about'),
    url(r'^addOffer/', views.addOffer, name='addOffer'),
    url(r'^addRequest/', views.addRequest, name='addRequest'),
]

