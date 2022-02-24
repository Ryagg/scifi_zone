from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='home'
    ),
    path(
        'site_notice/',
        views.site_notice,
        name='site_notice'
    ),
    path(

        'privacy_policy/',
        views.privacy_policy,
        name='privacy_policy'
    ),
    path(
        'timetable/',
        views.timetable,
        name='timetable'
    )
]
