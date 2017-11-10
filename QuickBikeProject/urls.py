from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # automatically generated documentation
    url(r'^docs/', include_docs_urls(title='RentBike API', description='RESTful API for RentBike')),
    # ? why needs 'namespase'
    url(r'^api/', include('RentBike.rest.urls', namespace='api_rentbike'))
]
