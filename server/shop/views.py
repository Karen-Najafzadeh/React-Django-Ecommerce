from rest_framework.generics import *
from rest_framework import viewsets, mixins
from shop.serializers import *
from shop import models

class Home(mixins.ListModelMixin,
           viewsets.GenericViewSet):
    """A view to get all the products to show on home page"""

    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer

class ProductView(mixins.ListModelMixin,
           viewsets.GenericViewSet):
    """a view to get all the products in the shop"""

    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCart(viewsets.ModelViewSet):
    """a view to manipulate shopping carts"""
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user.id
            queryset = models.Cart.objects.filter(user_id = user)
            return queryset
    serializer_class = ShoppingCartSerializer
        

# class ProfileView(viewsets.ModelViewSet):

#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             user = self.request.user.id
#             queryset = models.Profile.objects.get(user_id = user)
#             return queryset
#         # elif self.request.user.is_anonymous:
#         #     return
#     serializer_class = ProfileSerializer

#     def create(self, request, *args, **kwargs):
#         pass

#     def destroy(self, request, *args, **kwargs):
#         pass