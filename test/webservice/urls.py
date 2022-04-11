from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.CityViewSet)
router1 = routers.DefaultRouter()
router1.register(r'', views.ShopViewSet)
router2 = routers.DefaultRouter()
router2.register(r'', views.StreetViewSet)


urlpatterns = [
    path('city/', include(router.urls)),
    #path('shop/', include(router1.urls)),
    #path('street/', include(router2.urls)),
    path('street/<int:city_id>/', views.find_streets),
    path('shop/<int:city>', views.shop_sort)
]