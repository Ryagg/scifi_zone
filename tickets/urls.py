from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tickets, name='tickets'),
    path('packages/', views.all_packages, name='packages'),
    path('<tickets_id>/', views.ticket_detail, name="ticket_detail"),
    path('<package_id>/',
         views.package_detail, name="package_detail"),
]
