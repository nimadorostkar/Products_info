from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets, filters, status, pagination, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

class Product_Info(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'type']
    search_fields = ['name', 'barcode']
    ordering_fields = ['id']
    def get(self, request, format=None):
        query = self.filter_queryset(models.Product.objects.all())
        serializer = serializers.ProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class Product_Img(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'type']
    search_fields = ['name', 'barcode']
    ordering_fields = ['id']
    def get(self, request, format=None):
        query = self.filter_queryset(models.Product.objects.all())
        serializer = serializers.ProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


