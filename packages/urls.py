from django.urls import path
from . import views

urlpatterns = [
    path('', views.packages, name='packages'),
    path('<int:categories_id>/', views.package_detail, name="package_detail")
]
