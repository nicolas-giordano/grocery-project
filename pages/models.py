from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    item = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.item
