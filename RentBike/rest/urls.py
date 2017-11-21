# from rest_framework import routers
from django.conf.urls import url
from . import views


# router = routers.DefaultRouter()
# router.register(r'shops', ShopViewSet)
#
# urlpatterns = router.urls

urlpatterns = [
    url(r'^readShops/$', views.readShops),
]
