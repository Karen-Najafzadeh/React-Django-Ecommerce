from django_filters.rest_framework import FilterSet
from shop import models

class ProductFilter(FilterSet):
    class Meta:
        model = models.Product
        fields = {'category':['exact'],'sub_category':['exact'],'price':['lt','gt']}