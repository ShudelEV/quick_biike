from django.shortcuts import render
from .models import Shop

# For REST
from rest_framework import viewsets
from RentBike.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


