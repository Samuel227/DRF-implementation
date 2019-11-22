
from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializers
from rest_framework import viewsets
from rest_framework.decorators import action


class OrderView(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     serializer_class = OrderSerializers
