from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        extra_kwargs= {'shows': {'default': None}}
        fields = ['url','pk', 'name', 'meal', 'location']