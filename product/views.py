from . import models
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
import re




chrt = [
    ['627', 'FE8D', 'FE8E', '0', '0'],
    ['628', 'FE8F', 'FE90', 'FE92', 'FE91'],
    ['62A', 'FE95', 'FE96', 'FE98', 'FE97'],
    ['62B', 'FE99', 'FE9A', 'FE9C', 'FE9B'],
    ['62C', 'FE9D', 'FE9E', 'FEA0', 'FE9F'],
    ['62D', 'FEA1', 'FEA2', 'FEA4', 'FEA3'],
    ['62E', 'FEA5', 'FEA6', 'FEA8', 'FEA7'],
    ['62F', 'FEA9', 'FEAA', '0', '0'],
    ['630', 'FEAB', 'FEAC', '0', '0'],
    ['631', 'FEAD', 'FEAE', '0', '0'],
    ['632', 'FEAF', 'FEB0', '0', '0'],
    ['633', 'FEB1', 'FEB2', 'FEB4', 'FEB3'],
    ['634', 'FEB5', 'FEB6', 'FEB8', 'FEB7']
]

def GetCharRow(value):
    for row in chrt:
        if value == row[0]:
            return (list(row))

def CharType(chr, next, back):
    if (GetCharRow(chr) == None):
        return (0)
    else:
        hasMiddle = GetCharRow(chr)[3] != '0'
        hasBegin = GetCharRow(chr)[4] != '0'

    if (GetCharRow(next) == None):
        hasNext = False
    else:
        hasNext = GetCharRow(next)[2] != '0'

    if (GetCharRow(back) == None):
        hasBack = False
    else:
        hasBack = GetCharRow(back)[4] != '0'

    if (hasNext & hasBack):
        if (hasMiddle):
            return (3)
        return (2)
    if (hasNext):
        if (hasBegin):
            return (4)
        return (1)
    if (hasBack):
        return (2)
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

            product_name_str = serializer.data['name']
            res = (re.sub('.', lambda x: r'% 04X' % ord(x.group()), product_name_str))
            data = res.split(' ')[1:];
            chrsCode = []
            # printing result
            for idx, x in enumerate(data[1:-1], start=1):
                typ = CharType(x, data[idx + 1], data[idx - 1])
                if (typ == 0):
                    xutf = x
                else:
                    xutf = str(GetCharRow(x)[typ])
                xutf = chr(int(xutf, 16)).encode('utf-8')
                xutf = str(xutf);
                xutf = xutf.replace(r'\x', ",0x")
                xutf = xutf.replace("b' ,", "")
                stsr = xutf.replace("'", "")
                if (stsr.startswith('b')):
                    stsr = hex(ord(stsr[1]))
                chrsCode.append(stsr)
            chrsCode.reverse()
            chrsStr = ""
            chrsStr = ','.join(chrsCode)

            output = chrsStr + '\n' + \
                     "{:,}".format(int(serializer.data['price'])) + '\n' + \
                     "{:,}".format(int(serializer.data['off_price'])) + '\n' + \
                     serializer.data['off_percent'] + '\n' + \
                     str(query.image.name)[9:]
            return HttpResponse(output, content_type="text/plain")
        except:
            return HttpResponse('null', content_type="text/plain")