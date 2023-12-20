from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Shoe, ShoeCategory, Client, Order
from .serializers import ShoeCategorySerializer, ShoeSerializer, OrderSerializer, ClientSerializer, UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
# from .custompermission import IsCurrentUserOwnerOrReadOnly
# Create your views here.


class ShoeCategoryList(generics.ListCreateAPIView):
    queryset = ShoeCategory.objects.all()
    serializer_class = ShoeCategorySerializer
    name = 'shoe-category-list'
    filter_fields = ['name_category']
    search_fields = ['name_category']
    ordering_fields = ['name_category']


class ShoeCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoeCategory.objects.all()
    serializer_class = ShoeCategorySerializer
    name = 'shoe-category-detail'


class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    name = 'shoe-list'
    filter_fields = ['name', 'shoe_category', 'producer', 'color', 'price', 'description']
    search_fields = ['name', 'shoe_category', 'producer']
    ordering_fields = ['producer', 'shoe_category', 'price']

    def perform_create(self, serializer):
        serializer.save()


class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    name = 'shoe-detail'


class ClientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='birthdate', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='birthdate', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ['from_birthdate', 'to_birthdate']


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = ClientFilter
    name = 'client-list'
    ordering_fields = ['last_name', 'address']


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    client_name = AllValuesFilter(field_name='client_last_name')

    class Meta:
        model = Order
        fields = ['min_price', 'max_price', 'client_name']


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_class = OrderFilter
    name = 'order-list'


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    @staticmethod
    def get(request, *args, **kwargs):
        return Response({'shoes': reverse(ShoeList.name, request=request),
                         'shoe-categories': reverse(ShoeCategoryList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'orders': reverse(OrderList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         })
