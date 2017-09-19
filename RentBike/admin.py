from django.contrib import admin

from .models import Profile, Shop, Bike, Accessory, \
    Price, ContactInfo, Company, Order


admin.site.register([Profile, Shop, Bike, Accessory,
                     Price, ContactInfo, Company, Order])

