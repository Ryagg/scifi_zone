from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_guests, name='guests'),
    path('<int:actors_id>', views.guest_detail, name='guest_detail'),
    path('add/', views.add_guest, name='add_guest'),
    path('edit/<int:actors_id>', views.edit_guest_info, name='edit_guest_info')
]
