from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    picture_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Orders(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
