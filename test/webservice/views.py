from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import City, Shop, Street
from .serializers import CitySerializer, ShopSerializer, StreetSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


def find_streets(request, city_id):
    id = request.GET.get("city_id")
    streets = Street.objects.filter(city_id=id)
    for street in streets:
        print(street)

def shop_sort(request):
    id = request.GET.get()
    shops = Shop.objects.filter(city_id=id)