from django.urls import path
from . import views

urlpatterns = [
    path('shoe-categories',views.ShoeCategoryList.as_view(), name=views.ShoeCategoryList.name),
    path('shoe-categories/<int:pk>',views.ShoeCategoryDetail.as_view(), name=views.ShoeCategoryDetail.name),
    path('shoes', views.ShoeList.as_view(), name=views.ShoeList.name),
    path('shoes/<int:pk>', views.ShoeDetail.as_view(), name=views.ShoeDetail.name),
    path('clients', views.ClientList.as_view(), name=views.ClientList.name),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('orders', views.OrderList.as_view(), name=views.OrderList.name),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]
