from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_guests, name='guests'),
    path('<int:actors_id>', views.guest_detail, name='guest_detail'),

]