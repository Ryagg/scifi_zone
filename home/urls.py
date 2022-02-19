from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='home'),
    path(
        'site_notice/',
        views.site_notice,
        name='site_notice')
]
