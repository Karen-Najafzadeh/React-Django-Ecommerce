from rest_framework.generics import *
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response  import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from shop.serializers import *
from shop import filters
from shop import models



class Home(mixins.ListModelMixin,
           viewsets.GenericViewSet):
    """A view to get all the products to show on home page"""

    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer



class ProductView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """a view to get all the products in the shop"""

    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['name']
    filterset_class = filters.ProductFilter
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




class ProfileView(viewsets.ViewSet):    

    """A view to show the user their profile"""
    def list(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user.id
            queryset = models.Profile.objects.get(user_id=user)
            serializer = ProfileSerializer(queryset)
            return Response(serializer.data)
        elif self.request.user.is_anonymous:
            return Response('sorry you are not authenticated, log in to your account to see your profile')
    

    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], name='Update Profile', permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        profile = models.Profile.objects.get(user_id=request.user.id)

        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

        elif request.method == 'PUT' or 'PATCH':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
