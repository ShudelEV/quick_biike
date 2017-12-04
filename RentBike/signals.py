from django.db.models.signals import pre_save, post_save, m2m_changed
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
@receiver(m2m_changed, sender=Order.bikes.through)
def mount_invoice(**kwargs):

    logging.debug("mount_invoice.kwargs: {}".format(kwargs))

    if kwargs['action'] in ['post_add', 'post_remove']:
        order = kwargs.pop('instance', None)
        bikes = order.bikes.all()
        time_period = order.time_to - order.time_from

        mount = 0.0

        # to mount week's price
        if time_period.days >= 7:
            week_count = int(time_period.days / 7)
            for bike in bikes:
                logging.debug("mount_invoice.bike.week_price: {}".format(bike.week_price))
                mount += week_count * bike.week_price
            time_period -= timedelta(days=7 * week_count)
            logging.debug(
                "mount_invoice.week: week_count: {}, time_period_after: {}, mount: {}".format(
                    week_count, time_period, mount)
            )

        # to mount day's price
        if time_period.days >= 1:
            pass

        # to create qset_object only for update() function
        qset_obj = Order.objects.filter(id=order.id)
        logging.debug("mount_invoice.UPDATE: {}".format(qset_obj.update(invoice=mount)))
