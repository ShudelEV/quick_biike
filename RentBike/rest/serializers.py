from rest_framework import serializers
from RentBike.models import Shop, Order


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'photo', 'contact_info', 'company')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'bikes', 'accessories', 'time_from', 'time_to', 'invoice')

