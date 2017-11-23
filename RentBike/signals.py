from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Order

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="***** %(asctime)s:%(levelname)s:%(message)s"
    )


# Receiver function: to mount the Order.invoice field
@receiver(post_save, sender=Order)
def mount_invoice(**kwargs):
    instance = kwargs['instance']

    #  mount invoice only when Order created
    if kwargs['created']:
        time_period = instance.time_to - instance.time_from

        logging.debug("mount_invoice.time_period: {}".format(time_period))

        for bike in instance.bikes.all():
            logging.debug("mount_invoice.if_not_update: {}".format(bike.weekend_price))

        instance.invoice = 1000
        instance.save()


