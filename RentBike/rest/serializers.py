from rest_framework import serializers
from RentBike.models import Shop, Bike, Order


class ShopSerializer(serializers.ModelSerializer):
    # to add O2M field
    # bikes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='bikes:bike-detail',
    #     read_only=True
    # )

    class Meta:
        model = Shop
        fields = ('id', 'name', 'photo', 'contact_info', 'company', 'bikes')


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ('id', 'name', 'photo', 'type', 'shop',
                  'workday_price', 'weekend_price', 'week_price', 'description')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'bikes', 'accessories', 'time_from', 'time_to', 'invoice')

