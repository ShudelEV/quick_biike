from django.contrib import admin

from .models import Shop, Bike, Accessory, Price, ContactInfo, Company, Order
from Profile.models import User


class BikesInLine(admin.TabularInline):
    model = Bike
    extra = 0


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [BikesInLine, ]


admin.site.register([User, Bike, Accessory, Price, ContactInfo, Company, Order])

