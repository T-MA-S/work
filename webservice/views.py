from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import *
from django.http import HttpResponse, JsonResponse

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


def index(request):
    return HttpResponse("<h1>Добро пожаловать</h1>")



def find_streets(request, city_id):
    streets = Street.objects.filter(city_id=city_id)
    json_response = '{"streets":['
    for street in streets:
        json_response += "{"
        json_response += f'"id":"{street.id}",'
        json_response += f'"name":"{street.name}",'
        json_response += f'"street_id":"{street.id}"'
        json_response += "}"
    json_response += ']}'
    return HttpResponse(json_response)


def make_json_for_shop(shop):
    response = "{"
    response += f'"id":"{shop.id}",'
    response += f'"name":"{shop.name}",'
    response += f'"city_id":"{shop.city_id}",'
    response += f'"street_id":"{shop.street_id}",'
    response += f'"house_number":"{shop.house_number}",'
    response += f'"open_time":"{shop.open_time}",'
    response += f'"close_time":"{shop.close_time}"'
    response += "}"
    return response

def shop_is_open(shop):
    time = datetime.time(datetime.now())

    if shop.open_time <= time <= shop.close_time:
        return True
    else:
        return False

def shop_sort(request):
    street_id = request.GET.get("street")
    city_id = request.GET.get("city")
    is_open = request.GET.get("open")


    if street_id and city_id:
        shops = Shop.objects.filter(city_id=city_id, street_id=street_id)
    if street_id:
        shops = Shop.objects.filter(city_id=city_id, street_id=street_id)
    elif street_id:
        shops = Shop.objects.filter(street_id=street_id)
    elif city_id:
        shops = Shop.objects.filter(city_id=city_id)
    else:
        shops = Shop.objects.all()

    json_response = '{"shops":['
    for shop in shops:
        print(shop_is_open(shop))

        if is_open == '1' and shop_is_open(shop):
            json_response += make_json_for_shop(shop)

        if (is_open == '0') and (not shop_is_open(shop)):
            json_response += make_json_for_shop(shop)

        elif is_open is None:
            json_response += make_json_for_shop(shop)

    json_response += ']}'
    return HttpResponse(json_response)