from rest_framework import serializers
from .models import Shop, City, Street
from django.db import models

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

