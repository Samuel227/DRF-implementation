from rest_framework import serializers
from .models import Personal

class RestSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Personal
        extra_kwargs= {'shows': {'default': None}}
        fields = ['url','pk', 'name', 'age', 'race', 'discipline', 'hobbies',]