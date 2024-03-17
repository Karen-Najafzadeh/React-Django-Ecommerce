from rest_framework.generics import *
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response  import Response
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
    

    def update(self, request, pk=None):
        # pk is the primary key of the user whose profile is being updated
        # request.data contains the updated profile data

        # Retrieve the user profile to update
        if self.request.user.is_authenticated:
            user = self.request.user.id
            user_profile = models.Profile.objects.get(user_id=user)

        # Update the user profile with the data from the request
        user_profile_data = request.data
        print(user_profile_data)
        # user_profile.some_field = user_profile_data.get('some_field', user_profile.some_field)
        # Update other fields as needed

        # Save the updated user profile
        # user_profile.save()

        return Response({'message': 'User profile updated successfully'})
