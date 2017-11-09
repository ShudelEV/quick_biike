from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from RentBike.models import Shop
from .serializers import ShopSerializer


# ? May be to use ReadOnlyModelViewSet
class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that return set of shops using filter:
    {
         filter:{
             order: {
                 from: <str(date)>,
                 to: <str(date),
             },
             bike: {
                 typeIds: <[int]>,
                 count: <int>
             }
         }
    }
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @list_route()
    def readShops(self, request):
        pass





