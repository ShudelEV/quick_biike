from django.db.models.signals import m2m_changed
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
        time_from = order.time_from
        time_to = order.time_to

        mount = 0.0

        # to mount week's price
        if (time_to.day - time_from.day) >= 7:
            week_count = int((time_to.day - time_from.day) / 7)
            for bike in bikes:
                mount += week_count * bike.price.week
            time_from += timedelta(days=7 * week_count)
            logging.debug(
                "mount_invoice.week: week_count: {}, time_period_after: {}, mount: {}".format(
                    week_count, time_from, mount)
            )

        # to mount day's price
        if (time_to.day - time_from.day) >= 1:
            while (time_to.day - time_from.day) >= 1:
                if time_from.isoweekday() in [1, 2, 3, 4, 5]:
                    for bike in bikes:
                        mount += bike.price.work_day
                else:
                    for bike in bikes:
                        mount += bike.price.weekend_day
                time_from += timedelta(days=1)
            logging.debug("mount_invoice.day: time_period_after: {}, mount: {}".format(time_from, mount))

        # to mount hour's price
        # three hour's price
        while (time_to.hour - time_from.hour) >= 3:
            if time_from.isoweekday() in [1, 2, 3, 4, 5]:
                for bike in bikes:
                    mount += bike.price.workday_three_hours
            else:
                for bike in bikes:
                    mount += bike.price.weekend_three_hours
            time_from += timedelta(hours=3)
        logging.debug("mount_invoice.three_hours: time_period_after: {}, mount: {}".format(time_from, mount))

        # one hour's price
        while (time_to.hour - time_from.hour) >= 1:
            if time_from.isoweekday() in [1, 2, 3, 4, 5]:
                for bike in bikes:
                    mount += bike.price.workday_one_hour
            else:
                for bike in bikes:
                    mount += bike.price.weekend_one_hour
            time_from += timedelta(hours=1)
        logging.debug("mount_invoice.one_hour: time_period_after: {}, mount: {}".format(time_from, mount))

        # to update the invoice field
        Order.objects.filter(id=order.id).update(invoice=mount)
