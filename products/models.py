from django.db import models
from django.core.validators import FileExtensionValidator
import os


class User(models.Model):
  UserID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)
  Email = models.EmailField(unique=True)
  Password = models.CharField(max_length=128)
  Address = models.CharField(max_length=255, blank=True)

class Category(models.Model):
  CategoryID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)

class Product(models.Model):
  ProductID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  Category = models.ForeignKey(Category, on_delete=models.CASCADE)
  Image = models.ImageField(upload_to='products/', blank=True)

class FoodItem(Product):
  Cuisine = models.CharField(max_length=255, blank=True)

class Order(models.Model):
  OrderID = models.AutoField(primary_key=True)
  UserID = models.ForeignKey(User, on_delete=models.CASCADE)
  OrderDate = models.DateTimeField(auto_now_add=True)
  STATUS_CHOICES = (
      ('Pending', 'Pending'),
      ('Processing', 'Processing'),
      ('Delivered', 'Delivered'),
      ('Cancelled', 'Cancelled'),
  )
  Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class OrderItem(models.Model):
  OrderItemID = models.AutoField(primary_key=True)
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)
  Quantity = models.PositiveIntegerField()
  Price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
  TransactionID = models.AutoField(primary_key=True)
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  PAYMENT_METHOD_CHOICES = (
      ('Credit Card', 'Credit Card'),
      ('Cash on Delivery', 'Cash on Delivery'),
  )
  PaymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
  Amount = models.DecimalField(max_digits=10, decimal_places=2)

class Delivery(models.Model):
  DeliveryID = models.AutoField(primary_key=True)
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  DeliveryPerson = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  STATUS_CHOICES = (
      ('Pending', 'Pending'),
      ('On the way', 'On the way'),
      ('Delivered', 'Delivered'),
  )
  DeliveryStatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
  DeliveryFee = models.DecimalField(max_digits=10, decimal_places=2)

class Reward(models.Model):
  RewardID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  PointsRequired = models.PositiveIntegerField()

class UserReward(models.Model):
  UserRewardID = models.AutoField(primary_key=True)
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  Reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
  EarnedDate = models.DateTimeField(blank=True, null=True)

class Coin(models.Model):
  CoinID = models.AutoField(primary_key=True)
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  Amount = models.PositiveIntegerField()

class Competition(models.Model):
  CompetitionID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  StartDate = models.DateTimeField()
 # EndDate
    #@property
    #def curmonth(self):
        # yr=date.today().year
        # mn=date.today().month
        # print(self.deadline, date.today())
        #if self.deadline<=date.today():
            # print('OVER')
            #return 'rgb(248, 233, 129)'
class Meta:
    managed = True
    def __str__(self):
        return str(self.name)