from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    article = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Order
        fields = ['id', 'client', 'article', 'created']

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']
