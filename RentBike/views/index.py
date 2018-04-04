from django.shortcuts import render
from django.http import HttpResponse
import json

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="***** %(asctime)s:%(levelname)s:%(message)s"
    )


# View for index page.
def page(request):
    return render(request, 'rent_bike/index.html')

