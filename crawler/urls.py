from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Main_page'),
    path('page', views.search, name='searched_page'),
]