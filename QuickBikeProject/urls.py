from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.documentation import include_docs_urls


urlpatterns = []

if settings.DEBUG:
    urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # automatically generated documentation
    # url(r'^docs/', include_docs_urls(title='RentBike API', description='RESTful API for RentBike')),
    url(r'^api/', include('Profile.urls', namespace='users')),
    url(r'^api/', include('RentBike.rest.urls', namespace='api_rentbike')),
] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [url(r'^', include('RentBike.urls', namespace='rent_bike'))]

# urlpatterns += staticfiles_urlpatterns()

