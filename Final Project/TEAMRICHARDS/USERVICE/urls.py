from django.conf.urls import url
from django.views import generic
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^addoffer/', views.addoffer, name='addoffer'),
    url(r'^addrequest/', views.addrequest, name='addrequest'),
    url(r'^edit/', views.ActivityUpdate.as_view(), name='edit'),
    url(r'^carpoolDetail/(?P<pk>\d+)$', views.carpoolDetailView.as_view(), name='carpool-Detail'),
    url(r'^tutorDetail/(?P<pk>\d+)$', views.tutorDetailView.as_view(), name='tutor-Detail'),
    url(r'^textbookDetail/(?P<pk>\d+)$', views.textbookDetailView.as_view(), name='textbook-Detail'),
    url(r'^activityDetail/(?P<pk>\d+)$', views.activityDetailView.as_view(), name='activity-Detail'),
    url(r'^profile/(?P<pk>\d+)$', views.profileDetailView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfileUpdate.as_view(), name='profile_Edit'),
    url(r'^searchoffer/$', views.offerListView.as_view(), name='searchoffer'),
    url(r'^searchrequest/$', views.requestListView.as_view(), name='searchrequest'),
    url(r'^mypublish/$', views.mypublishListView.as_view(), name='mypublish'),
    url(r'^activity/create_request/$', views.ActivityCreateRequest.as_view(), name='activity-Create-r'),
    url(r'^activity/create_offer/$', views.ActivityCreateOffer.as_view(), name='activity-Create-o'),
    url(r'^activity/(?P<pk>\d+)/update/$', views.ActivityUpdate.as_view(), name='activity-Edit'),
    url(r'^activity/(?P<pk>\d+)/delete/$', views.ActivityDelete.as_view(), name='activity_delete'),
    url(r'^carpool/create_request/$', views.CarpoolCreateRequest.as_view(), name='carpool-Create-r'),
    url(r'^carpool/create_offer/$', views.CarpoolCreateOffer.as_view(), name='carpool-Create-o'),
    url(r'^carpool/(?P<pk>\d+)/update/$', views.CarpoolUpdate.as_view(), name='carpool-Edit'),
    url(r'^carpool/(?P<pk>\d+)/delete/$', views.CarpoolDelete.as_view(), name='carpool_delete'),
    url(r'^tutor/create_request/$', views.TutorCreateRequest.as_view(), name='tutor-Create-r'),
    url(r'^tutor/create_offer/$', views.TutorCreateOffer.as_view(), name='tutor-Create-o'),
    url(r'^tutor/(?P<pk>\d+)/update/$', views.TutorUpdate.as_view(), name='tutor-Edit'),
    url(r'^tutor/(?P<pk>\d+)/delete/$', views.TutorDelete.as_view(), name='tutor_delete'),
    url(r'^textbook_trading/create_request/$', views.Textbook_TradingCreateRequest.as_view(), name='textbook-Create-r'),
    url(r'^textbook_trading/create_offer/$', views.Textbook_TradingCreateOffer.as_view(), name='textbook-Create-o'),
    url(r'^textbook_trading/(?P<pk>\d+)/update/$', views.Textbook_TradingUpdate.as_view(), name='textbook-Edit'),
    url(r'^textbook_trading/(?P<pk>\d+)/delete/$', views.Textbook_TradingDelete.as_view(), name='textbook_trading_delete'),
    url(r'^textbook/(?P<pk>\d+)/comment/$', views.add_comment_to_book, name='add_comment_to_book'),
    url(r'^carpool/(?P<pk>\d+)/comment/$', views.add_comment_to_carpool, name='add_comment_to_carpool'),
    url(r'^tutor/(?P<pk>\d+)/comment/$', views.add_comment_to_tutor, name='add_comment_to_tutor'),
    url(r'^activity/(?P<pk>\d+)/comment/$', views.add_comment_to_activity, name='add_comment_to_activity'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


]
