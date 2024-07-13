import django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.views.decorators.csrf import csrf_exempt
from .views import add_to_cart, view_cart


urlpatterns=[
    #path('view-attendance', views.viewAttendance, name="view-attendance"),
    path('', views.index, name="product-home"),
    path('add-product', views.add_product, name="add-product"),
    path('customer-info', views.customerinfo, name="customer-info"),
    path('seller-det', views.sellerinfo, name="seller-det"),
    path('checkout-det', views.checkout, name="checkout-det"),
    path("shop-details", views.shopDetails, name="shop-details"),
    path('contactus', views.contactus, name="contactus"),
    path('cart', views.Cart, name="cart"),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
   path('signup', views.signup, name="signup"),
]