from django.urls import path
from . import views

urlpatterns = [
    path('ads', views.Advertise.as_view(), name='ads'),
]
