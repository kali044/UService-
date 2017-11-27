from django.conf.urls import url
from django.views import generic

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^addoffer/', views.addoffer, name='addoffer'),
    url(r'^addrequest/', views.addrequest, name='addrequest'),
    url(r'^edit/(?P<pk>\d+)', views.ActivityUpdate.as_view(), name='edit'),
    url(r'^carpoolDetail/(?P<pk>\d+)$', views.carpoolDetailView.as_view(), name='carpool-Detail'),
    url(r'^tutorDetail/(?P<pk>\d+)$', views.tutorDetailView.as_view(), name='tutor-Detail'),
    url(r'^textbookDetail/(?P<pk>\d+)$', views.textbookDetailView.as_view(), name='textbook-Detail'),
    url(r'^activityDetail/(?P<pk>\d+)$', views.activityDetailView.as_view(), name='activity-Detail'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^searchoffer/$', views.offerListView.as_view(), name='searchoffer'),
    url(r'^searchrequest/$', views.requestListView.as_view(), name='searchrequest'),
    url(r'^mypublish/$', views.mypublishListView.as_view(), name='mypublish'),
    url(r'^activity/create/$', views.ActivityCreate.as_view(), name='activity_create'),
    url(r'^activity/(?P<pk>\d+)/update/$', views.ActivityUpdate.as_view(), name='activity_update'),
    url(r'^activity/(?P<pk>\d+)/delete/$', views.ActivityDelete.as_view(), name='activity_delete'),
    url(r'^carpool/create/$', views.CarpoolCreate.as_view(), name='carpool_create'),
    url(r'^carpool/(?P<pk>\d+)/update/$', views.CarpoolUpdate.as_view(), name='carpool_update'),
    url(r'^carpool/(?P<pk>\d+)/delete/$', views.CarpoolDelete.as_view(), name='carpool_delete'),
    url(r'^tutor/create/$', views.TutorCreate.as_view(), name='tutor_create'),
    url(r'^tutor/(?P<pk>\d+)/update/$', views.TutorUpdate.as_view(), name='tutor_update'),
    url(r'^tutor/(?P<pk>\d+)/delete/$', views.TutorDelete.as_view(), name='tutor_delete'),
    url(r'^textbook_trading/create/$', views.Textbook_TradingCreate.as_view(), name='textbook_trading_create'),
    url(r'^textbook_trading/(?P<pk>\d+)/update/$', views.Textbook_TradingUpdate.as_view(), name='textbook_trading_update'),
    url(r'^textbook_trading/(?P<pk>\d+)/delete/$', views.Textbook_TradingDelete.as_view(), name='textbook_trading_delete'),
]
