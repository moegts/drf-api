from rest_framework import serializers

from .models import CoffeHouse


class coffeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'drink', 'description', 'cheff', 'created_at')
        model = CoffeHouse