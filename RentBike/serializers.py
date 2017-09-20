from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    photo = serializers.URLField()
#    contact_info = serializers.ManyRelatedField()

    def create(self, validated_data):
        """
        Create and return a new `Shop` instance, given the validated data.
        """
        return Shop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Shop` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

