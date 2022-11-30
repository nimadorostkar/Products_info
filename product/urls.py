from django.urls import path
from . import views

urlpatterns = [
    path('info', views.Product_Info.as_view(), name='info'),
    path('img', views.Product_Img.as_view(), name='img'),
]
