from rest_framework import routers
from django.conf.urls import url
from . import views


router = routers.DefaultRouter()
router.register(r'shops', views.ShopViewSet, r'shop')
router.register(r'orders', views.OrderViewSet, r'order')

urlpatterns = router.urls

urlpatterns += [
    url(r'^readShops/$', views.readShops),
    url(r'^createOrder/$', views.createOrder),
]
