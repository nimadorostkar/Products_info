from django.urls import path
from . import views

urlpatterns = [
    path('product', views.Product_Info.as_view(), name='product'),
]
