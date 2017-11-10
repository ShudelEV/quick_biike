from django.contrib import admin

from .models import Shop, Bike, Accessory, \
    Price, ContactInfo, Company, Order
from Profile.models import User


admin.site.register([User, Shop, Bike, Accessory,
                     Price, ContactInfo, Company, Order])

