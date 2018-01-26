from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # automatically generated documentation
    url(r'^docs/', include_docs_urls(title='RentBike API', description='RESTful API for RentBike')),
    # ? why needs 'namespase'
    url(r'^api/', include('Profile.urls', namespace='users')),
    url(r'^api/', include('RentBike.rest.urls', namespace='api_rentbike')),
]

# urlpatterns += staticfiles_urlpatterns()

urlpatterns += [url(r'^', include('RentBike.urls', namespace='rent_bike'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
