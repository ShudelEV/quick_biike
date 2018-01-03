from django.shortcuts import render
from django.http import HttpResponse
import json
from RentBike.forms import PrevOrderForm

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="***** %(asctime)s:%(levelname)s:%(message)s"
    )


# View for index page.
def page(request):
    if request.POST:
        form = PrevOrderForm(request.POST)
        if form.is_valid():
            logging.debug("valid data: {}".format(request.POST))
            return HttpResponse('Order created!')
        else:
            logging.debug("valid data: {}".format(request.POST))
            return HttpResponse('Not valid data!')
    else:
        return render(request, 'rent_bike/index.html', {'form': PrevOrderForm()})


def prev_order(request):
    logging.debug("prev_order: {}".format(request.POST))
    return HttpResponse(json.dumps('1'), content_type="application/json")
