from django.contrib import admin
from .models import Shoe, ShoeCategory, Client, Order

# Register your models here.
# admin.site.register(Shoe)

admin.site.register(ShoeCategory)
admin.site.register(Client)
admin.site.register(Order)


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ["name", "producer", "shoe_category", "price"]
    list_filter = ["producer", "shoe_category"]
    search_fields = ["name", "producer", "shoe_category"]
