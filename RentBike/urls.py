from django.conf.urls import url
from .views import index


urlpatterns = [
    url(r'^', index.page, name='index'),
    # url(r'^index$', index.page),
]