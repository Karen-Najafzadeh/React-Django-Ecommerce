from rest_framework.serializers import ModelSerializer
from shop import models

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
    
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

class ShoppingCartSerializer(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'