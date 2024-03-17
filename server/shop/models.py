from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/image', null=True, blank=True)
    favorites = models.ManyToManyField('Product', blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        



class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Product(models.Model):
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
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.CharField(
        max_length=1, choices=SUB_CATEGORY_CHOICES
    )
    image = models.ImageField(upload_to='products/image')
    likes = models.PositiveIntegerField()


    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    



class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)