from django.conf.urls import url
from .views import index, order


urlpatterns = [
    url(r'^', index.page, name='index'),
    url(r'^index$', index.page),
    url(r'^prev_order/$', index.prev_order, name='prev_order'),
]
