from django.urls import path
from . import views

urlpatterns = [
    path('', views.find, name='search_results'),
]
