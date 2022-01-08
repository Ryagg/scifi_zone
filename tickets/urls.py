from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tickets, name='tickets'),
    path('<tickets_id>', views.ticket_detail, name="ticket_detail")
]