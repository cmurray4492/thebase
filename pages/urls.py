"""URLs file for my Pages App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    # path('contactus', views.contactus, name="contactus"),
    # path('usefulinfo', views.usefulinfo, name="usefulinfo"),
]
