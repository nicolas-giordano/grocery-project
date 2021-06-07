from django.contrib import admin
from .models import Store, Item, StoreItems
# Register your models here.

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(StoreItems)
