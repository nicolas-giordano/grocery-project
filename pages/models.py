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


class StoreItems(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    price_per_lb = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return f"Store: {self.store}, Item: {self.item}"
