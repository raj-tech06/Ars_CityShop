from django.db import models

# Create your models here.

from django.db import models

class CustomAdmin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=200)
    shop_address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
