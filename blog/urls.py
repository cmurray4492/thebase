"""URLs file for my HR Blog App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:blog_id>/<str:blog_slug>',
         views.blogarticle, name='blogarticle'),
    # path('search', views.search, name='search'),
]
