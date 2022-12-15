from . import models
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
import csv
import re

chrt = [
['627', 'FE8D', 'FE8E', 'FE8E', 'FE8D', 0],
['628', 'FE8F', 'FE90', 'FE92', 'FE91', 1],
['62A', 'FE95', 'FE96', 'FE98', 'FE97', 1],
['62B', 'FE99', 'FE9A', 'FE9C', 'FE9B', 1],
['62C', 'FE9D', 'FE9E', 'FEA0', 'FE9F', 1],
['62D', 'FEA1', 'FEA2', 'FEA4', 'FEA3', 1],
['62E', 'FEA5', 'FEA6', 'FEA8', 'FEA7', 1],
['62F', 'FEA9', 'FEAA', 'FEAA', 'FEA9', 0],
['630', 'FEAB', 'FEAC', 'FEAC', 'FEAB', 0],
['631', 'FEAD', 'FEAE', 'FEAE', 'FEAD', 0],
['632', 'FEAF', 'FEB0', 'FEB0', 'FEAF', 0],
['633', 'FEB1', 'FEB2', 'FEB4', 'FEB3', 1],
['634', 'FEB5', 'FEB6', 'FEB8', 'FEB7', 1],
['635', 'FEB9', 'FEBA', 'FEBC', 'FEBB', 1],
['636', 'FEBD', 'FEBE', 'FEC0', 'FEBF', 1],
['637', 'FEC1', 'FEC2', 'FEC4', 'FEC3', 1],
['638', 'FEC5', 'FEC6', 'FEC8', 'FEC7', 1],
['639', 'FEC9', 'FECA', 'FECC', 'FECB', 1],
['63A', 'FECD', 'FECE', 'FED0', 'FECF', 1],
['641', 'FED1', 'FED2', 'FED4', 'FED3', 1],
['642', 'FED5', 'FED6', 'FED8', 'FED7', 1],
['6A9', 'FED9', 'FEDA', 'FEDC', 'FEDB', 1],
['644', 'FEDD', 'FEDE', 'FEE0', 'FEDF', 1],
['645', 'FEE1', 'FEE2', 'FEE4', 'FEE3', 1],
['646', 'FEE5', 'FEE6', 'FEE8', 'FEE7', 1],
['647', 'FEE9', 'FEEA', 'FEEC', 'FEEB', 1],
['648', 'FEED', 'FEEE', 'FEEE', 'FEED', 0],
['64A', 'FEF1', 'FEF2', 'FEF4', 'FEF3', 1],
['622', 'FE81', 'FE82', 'FE82', 'FE81', 1],
['629', 'FE93', 'FE94', 'FE94', 'FE93', 1],
['649', 'FEEF', 'FEF0', 'FEF0', 'FEEF', 1],
['6AF', 'FB92', 'FB93', 'FB95', 'FB94', 1],
['686', 'FB7A', 'FB7B', 'FB7D', 'FB7C', 1],
['67E', 'FB56', 'FB57', 'FB59', 'FB58', 1],
['698', 'FB8A', 'FB8B', 'FB8B', 'FB8A', 0],
['6CC', 'FEEF', 'FEF0', 'FEF4', 'FEF3', 0]
]


def GetCharRow(value):
    for row in chrt:
        if value == row[0]:
            return (list(row))


def CharType(chr, next, back):
    if (GetCharRow(chr) == None):
        return (0)

    if (GetCharRow(next) == None):
        hasNext = False
    else:
        hasNext = True

    if (GetCharRow(back) == None):
        hasBack = False
    else:
        hasBack = (GetCharRow(back)[5] == 1)

    if (hasNext) and (hasBack):
        return (3)

    if (hasNext) and (not hasBack):
        return (4)

    if (not hasNext) and (hasBack):
        return (2)

    if (not hasNext) and (not hasBack):
        return (1)





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

            test_str = serializer.data['name']
            test_str = " " + test_str + " "
            res = (re.sub('.', lambda x: r'% 04X' % ord(x.group()), test_str))
            data = res.split(' ')[1:];
            chrsCode = []
            utf32name = ""
            for idx, x in enumerate(data[1:-1], start=1):
                typ = CharType(x, data[idx + 1], data[idx - 1])
                if (typ == 0):
                    xutf = x
                else:
                    xutf = str(GetCharRow(x)[typ])
                utf32name += chr(int(xutf, 16))
            for s in utf32name.split():
                if s.isdigit():
                    utf32name = utf32name.replace(s, s[::-1])
            product_name = utf32name[::-1]
            #product_name = utf32name

            output = product_name + '\n' + \
                     "{:,}".format(int(serializer.data['price'])) + '\n' + \
                     "{:,}".format(int(serializer.data['off_price'])) + '\n' + \
                     serializer.data['off_percent'] + '\n' + \
                     "/"+str(query.image.name)[9:]
            return HttpResponse(output, content_type="text/plain")
        except:
            return HttpResponse('null', content_type="text/plain")