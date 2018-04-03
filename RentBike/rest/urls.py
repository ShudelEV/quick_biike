from rest_framework import routers
from django.conf.urls import url
from . import views


router = routers.DefaultRouter()
router.register(r'shops', views.ShopViewSet, r'shop')
router.register(r'bikes', views.BikeViewSet, r'bike')
router.register(r'orders', views.OrderViewSet, r'order')

urlpatterns = router.urls

urlpatterns += [
    url(r'^readShops/$', views.read_shops),
    url(r'^readBikes/$', views.read_bikes),
    url(r'^createOrder/$', views.create_order),
]
