from django.contrib import admin
from store.models import Customer, Category, Product, Order

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
