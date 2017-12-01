from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import timedelta

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
    order = kwargs['instance']
    bikes = order.bikes.all()
    time_period = order.time_to - order.time_from

    # if bikes.exists():
    #     logging.debug("mount_invoice.bikes: {}: {}".format('EXIST', bikes))
    # else:
    #     logging.debug("mount_invoice.bikes: {}".format('NOT EXIST'))

    logging.debug("mount_invoice.time_period: {}, order: {}, bikes: {}".format(time_period, order, bikes))

    mount = 0.0

    if time_period.days >= 7:
        week_count = int(time_period.days / 7)
        for bike in bikes:
            logging.debug("mount_invoice.bike.week_price: {}".format(bike.week_price))
            mount += week_count * bike.week_price
        time_period -= timedelta(days=7*week_count)
        logging.debug(
            "mount_invoice.week: week_count: {}, time_period_after: {}, mount: {}".format(
                week_count, time_period, mount)
        )

    # for bike in instance.bikes.all():
    #     logging.debug("mount_invoice.if_not_update: {}".format(bike.weekend_price))

    order.invoice = mount
    order.update()

