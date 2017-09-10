from django.db import models


class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_info = models.ForeignKey(ContactInfo)


class Company(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField(verbose_name="company photo")
    contact_info = models.ForeignKey(ContactInfo)


class Shop(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField(verbose_name="shop photo")
    contact_info = models.ForeignKey(ContactInfo)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Price(models.Model):
    one_hour = models.FloatField(verbose_name="price for an hour")
    three_hours = models.FloatField(verbose_name="price for three hours")
    day = models.FloatField(verbose_name="price for a day")
    week = models.FloatField(verbose_name="price for a week")


class Bike(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField()
    TYPE = (('1', 'male'), ('2', 'female'), ('3', 'children\'s'))
    type = models.CharField(max_length=1, choices=TYPE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    workday_price = models.ForeignKey(Price)
#    weekend_price = models.ForeignKey(Price)
    state = models.BooleanField()

    def __str__(self):
        return self.name


class Accessory(models.Model):
    name = models.CharField(max_length=200)
    price = models.ForeignKey(Price)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Order(models.Model):

    def mount_invoice(self):
        pass

    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bikes = models.ManyToManyField(Bike)
    accessories = models.ManyToManyField(Accessory)
    time_from = models.DateTimeField(verbose_name="from")
    time_to = models.DateTimeField(verbose_name="to")
    invoice = models.FloatField()
