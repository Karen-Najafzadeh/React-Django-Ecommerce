from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/image', null=True, blank=True)
    favorites = models.ManyToManyField('Product')



class Category(models.Model):
    name = models.CharField(max_length=50)



class Product(models.Model):
    PRODUCT_STATUS_IN_STOCK = 'I'
    PRODUCT_STATUS_SOLD_OUT = 'O'

    PRODUCT_STATUS_CHOICES = [
        (PRODUCT_STATUS_IN_STOCK, 'In Stock'),
        (PRODUCT_STATUS_SOLD_OUT, 'Sold Out')
    ]

    SUB_CATEGORY_BAG = 'B'
    SUB_CATEGORY_SHOE = 'S'
    SUB_CATEGORY_CLOTH = 'C'
    SUB_CATEGORY_PANTS = 'P'

    SUB_CATEGORY_CHOICES = [
        (SUB_CATEGORY_CLOTH, 'Cloths'),
        (SUB_CATEGORY_PANTS, 'Pants'),
        (SUB_CATEGORY_SHOE, 'Shoes'),
        (SUB_CATEGORY_BAG, 'Bags')
    ]

    
    name = models.CharField(max_length=100)
    description = models.TextField()
    in_stock = models.CharField(
        max_length=1, choices=PRODUCT_STATUS_CHOICES, 
        default=PRODUCT_STATUS_IN_STOCK
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.CharField(
        max_length=1, choices=SUB_CATEGORY_CHOICES
    )
    image = models.ImageField(upload_to='products/image')
    likes = models.PositiveIntegerField()



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)



class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()