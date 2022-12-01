from . import models
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
import re
from django.http import FileResponse


class Product_Info(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        try:
            barcode = request.GET.get('barcode')
        except:
            return Response("Add barcode in parameters", status=status.HTTP_400_BAD_REQUEST)
        try:
            query = models.Product.objects.get(barcode=barcode)
            serializer = serializers.ProductSerializer(query)
            res = ''.join(r'{:04X},'.format(ord(chr)) for chr in serializer.data['name'])
            output =  str(res) + '\n' + serializer.data['price'] + '\n' + serializer.data['off_price'] + '\n' + serializer.data['off_percent']
            return HttpResponse(output, content_type="text/plain", status=status.HTTP_200_OK)
        except:
            return Response("There is no product with this barcode", status=status.HTTP_400_BAD_REQUEST)



class Product_Img(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        try:
            barcode = request.GET.get('barcode')
        except:
            return Response("Add barcode in parameters", status=status.HTTP_400_BAD_REQUEST)
        query = models.Product.objects.get(barcode=barcode)
        return FileResponse(query.image, content_type="application/force-download", status=status.HTTP_200_OK)

