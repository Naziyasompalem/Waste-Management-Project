from django.contrib import admin
from .models import *
from .models import Customer


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
admin.site.register(ExtraItem)