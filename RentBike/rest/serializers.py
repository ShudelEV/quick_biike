from rest_framework import serializers
from RentBike.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'photo', 'contact_info', 'company')

