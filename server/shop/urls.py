from django.urls import path, include
from shop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('home',views.Home, basename='home_page')
router.register('products',views.ProductView, basename='all_products')
router.register('cart',views.ShoppingCart, basename='my_shopping_carts')
router.register('profile',views.ProfileView, basename='my_profile')




urlpatterns =[
    path('',include(router.urls)),

]