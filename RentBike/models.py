from django.db import models
from Profile.models import User


class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address


class Company(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField(verbose_name="company photo")
    contact_info = models.ForeignKey(ContactInfo)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField(verbose_name="shop photo")
    contact_info = models.ForeignKey(ContactInfo)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Price(models.Model):
    workday_one_hour = models.FloatField(verbose_name="price for an hour (workday)", default=0)
    workday_three_hours = models.FloatField(verbose_name="price for three hours (workday)", default=0)
    work_day = models.FloatField(verbose_name="price for a day (workday)", default=0)
    weekend_one_hour = models.FloatField(verbose_name="price for an hour (weekend)", default=0)
    weekend_three_hours = models.FloatField(verbose_name="price for three hours (weekend)", default=0)
    weekend_day = models.FloatField(verbose_name="price for a day (weekend)", default=0)
    week = models.FloatField(verbose_name="price for a week", default=0)


class Bike(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField()
    type = models.CharField(max_length=1,
                            choices=(('1', 'male'), ('2', 'female'), ('3', 'children\'s')),
                            default='1')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.ForeignKey(Price)
    state = models.BooleanField(verbose_name="busy")

    def __str__(self):
        return self.name


class Accessory(models.Model):
    name = models.CharField(max_length=200)
    price = models.ForeignKey(Price)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):

    def mount_invoice(self):
        pass

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    bikes = models.ManyToManyField(Bike)
    accessories = models.ManyToManyField(Accessory)
    time_from = models.DateTimeField(verbose_name="from")
    time_to = models.DateTimeField(verbose_name="to")
    invoice = models.FloatField()
