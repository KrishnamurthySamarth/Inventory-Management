from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory_items(models.Model):
    item_name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    Unit_price = models.IntegerField()
    dispatched_from = models.CharField(max_length=250) 
    dispatched_price = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)