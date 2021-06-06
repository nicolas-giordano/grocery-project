from django.db import models

# Create your models here.


# Table for stores that are supported
class Stores(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Table for common grocery items
class Items(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.item
