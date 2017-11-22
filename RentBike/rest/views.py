from rest_framework import viewsets, status
from rest_framework.decorators import api_view, list_route, detail_route
from rest_framework.response import Response
from RentBike.models import Shop, Order
from .serializers import ShopSerializer, OrderSerializer


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that return set of shops
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


@api_view(['POST'])
def readShops(request):
    """
        API endpoint that return set of shops using filter:
    {
         "filter":{
             "busy_bike": {
                 "from": <str(date)>,
                 "to": <str(date)>
             },
             "bike": {
                 "typeIds": <[int]>,
                 "count": <int>
             }
         }
    }
    """
    try:
        filter_data = request.data['filter']
    except KeyError as err:
        return Response("detail: Not valid content!", status.HTTP_400_BAD_REQUEST)
    else:
        return Response(filter_data)

    shops = Shop.objects.all()

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that return set of shops
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['POST'])
def createOrder(request):
    """
        API endpoint that create order using request:
    {
        "bikeIds": <[int]>,
        "from": <str(date)>,
        "to": <str(date)>
    }
    """
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
