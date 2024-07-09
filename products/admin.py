from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(Delivery)
admin.site.register(Reward)
admin.site.register(UserReward)
admin.site.register(Coin)
admin.site.register(Competition)
admin.site.register(Seller)
admin.site.register(ShippingInformation)