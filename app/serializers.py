from rest_framework import serializers
from .models import ShoeCategory, Shoe, Client, Order
from django.contrib.auth.models import User


class ShoeCategorySerializer(serializers.HyperlinkedModelSerializer):
    shoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='shoe-detail')

    class Meta:
        model = ShoeCategory
        fields = ['pk', 'url', 'name_category', 'shoes']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    shoe_category = serializers.SlugRelatedField(queryset=ShoeCategory.objects.all(), slug_field='name_category')
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='order-detail')

    class Meta:
        model = Shoe
        fields = ['url', 'name', 'shoe_category', 'producer', 'gender', 'color', 'price', 'description', 'image', 'orders']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='order-detail')
    gender = serializers.ChoiceField(choices=Client.GENDER_CHOICES)

    class Meta:
        model = Client
        fields = ['pk', 'url', 'first_name', 'last_name', 'gender', 'address', 'birthdate', 'added_time', 'orders']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='last_name')
    shoe = serializers.SlugRelatedField(queryset=Shoe.objects.all(), slug_field='name')

    class Meta:
        model = Order
        fields = ['pk', 'url', 'client', 'shoe', 'price', 'quantity']

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise serializers.ValidationError("Price lower or equal to zero", )
        return value

    @staticmethod
    def validate_quantity(value):
        if value <= 0:
            raise serializers.ValidationError("Quantity lower or equal to zero", )
        return value


class UserShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    shoes = UserShoeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'shoes']
