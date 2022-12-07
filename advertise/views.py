from . import models
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

class Advertise(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        try:
            base_url=request.META['HTTP_HOST']
            ads_list=[]
            ads = models.Advertise.objects.all()
            for add in ads:
                ads_list.append(base_url+add.image.url+'\n')
            return HttpResponse(ads_list, content_type="text/plain")
        except:
            return HttpResponse('null', content_type="text/plain")