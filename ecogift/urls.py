"""
URL configuration for ecogift project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.views.decorators.csrf import csrf_exempt
from products import views as products_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_views.index, name="index"),
    path('shop', views.shop, name="shop"),
    #path('register', views.registerPage, name="register"),
    path('loginCus', views.customerLogin, name="loginCus"),
    path('logout', views.customerLogout, name="logoutCus"),
    path('fcomp',views.fcompPage, name="fcomp"),
    path('successPage',views.paymentSuccessPage, name="successPage"),
    path('Myorders', views.My_Orders, name="Myorders"),
    path('products/',include('products.urls')),
    path('myaccount', views.myaccountPage, name="myaccount"),
    path('seller-main',views.sellerMain,name="seller-main"),
    path("DeleteProduct/<int:product_id>", views.deleteProductPage, name="DeleteProduct"),
    path('Donate',views.Donatepg,name="Donate"),
    path('prices',views.Pricelist,name="prices"),
    path('notify',views.Notification,name="notify"),
    path('Generator',views.SellerDet,name="Generator"),
]


urlpatterns+= staticfiles_urlpatterns() 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)