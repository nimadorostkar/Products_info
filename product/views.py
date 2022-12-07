from . import models
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

class Product_Info(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        try:
            barcode = request.GET.get('barcode')
        except:
            return HttpResponse('null', content_type="text/plain")
        try:
            query = models.Product.objects.get(barcode=barcode)
            serializer = serializers.ProductSerializer(query)
            print('---------')

            output = serializer.data['name'] + '\n' + \
                     "{:,}".format(int(serializer.data['price'])) + '\n' + \
                     "{:,}".format(int(serializer.data['off_price'])) + '\n' + \
                     serializer.data['off_percent'] + '\n' + \
                     str(query.image.name)[9:]
            return HttpResponse(output, content_type="text/plain")
        except:
            return HttpResponse('null', content_type="text/plain")