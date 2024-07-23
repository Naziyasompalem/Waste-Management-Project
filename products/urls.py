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
    path("shop-details/<int:product_id>", views.shopDetails, name="shop-details"),
    path('contactemail', views.contactus_request, name="contactemail"),
    path('contactus', views.contactus, name="contactus"),
    path('cart', views.view_cart, name="cart"),
    path('change_quantity/<int:cartItem_id>/<int:quantity>', views.increment_product, name="increment"),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('discardItem/<int:CartItem_id>',views.DiscardItem, name="discardItem"),
    path('signup', views.signup, name="signup"),
    path('mapbox', views.mapbox_api_call, name="mapbox"),
    path('add_query', views.add_query, name="add_query"),
    path('checkout', views.checkout_call, name="checkout"),
    path('successPage',views.paymentSuccessPage, name="successPage"),
    #path('bulkdata', views.bulkdata_call, name="bulkdata"),
    path('search', views.search, name="search"),
    path('accept-query/<int:Query_id>', views.accept_query, name="accept_query"),
    path('decline-query/<int:Query_id>', views.decline_query, name="decline_query"),
]