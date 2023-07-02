from django.contrib import admin
from django.urls import path
from ThrottleAction import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("review",views.review,name='review'),
    path("exclusive",views.exclusive,name='exclusive'),
    path("privacy",views.privacy,name='privacy'),
    path("terms",views.terms,name='terms'),
    path("contact",views.contact,name='contact'),
    path("consult",views.consult,name='consult'),
    path("showreview/<slug>/",views.showreview,name='showreview'),
    path("showexclusive/<slug>/",views.showexclusive,name='showexclusive'),
    path("contactform",views.contactform,name='contactform'),
    path("subscribe",views.subscribe,name='subscribe'),
    path("error_400",views.error_400,name='error_400'),
    path("error_404",views.error_404,name='error_404'),
    path("error_403",views.error_403,name='error_403'),
    path("error_500",views.error_500,name='error_500'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)