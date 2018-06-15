from rest_framework import serializers
from RentBike.models import Shop, Bike, Order


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        depth = 2


class ShopWithBikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'photo', 'contact_info', 'company', 'bikes')
        depth = 2


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'
        depth = 2


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'bikes', 'accessories', 'time_from', 'time_to', 'invoice')
