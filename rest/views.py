from django.shortcuts import render
from rest.models import Personal
from rest.serializers import RestSerializers
from rest_framework import viewsets
from rest_framework.decorators import action

# from rest_framework import generics
# # Create your views here.

class Rest(viewsets.ModelViewSet):
     queryset = Personal.objects.all()
     serializer_class = RestSerializers

     
     
'''
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def rest_list(request):
    
    if request.method == 'GET':
        queryset = Personal.objects.all()
        serializer = RestSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = RestSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
