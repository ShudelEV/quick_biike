from rest_framework import viewsets, status
from rest_framework.decorators import api_view, list_route, detail_route
from rest_framework.response import Response
from RentBike.models import Shop, Order, Bike
from .serializers import ShopSerializer, OrderSerializer

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


def bad_request(err_massage):
    return Response(err_massage, status=status.HTTP_400_BAD_REQUEST)


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
                 "time_from": <str(date)>,
                 "time_to": <str(date)>
             },
             "bike_count": {
                 "type1": <int>,
                 "type2": <int>,
                 "type3": <int>
                 }
             }
         }
    }
    """
    try:
        filter_data = request.data['filter']

        logging.debug("REST.readShops: filter: {}".format(filter_data))

        time_from = filter_data['busy_bike']['time_from']
        time_to = filter_data['busy_bike']['time_to']
        bike_count = filter_data['bike_count']

    except KeyError as err:
        return bad_request("detail: Not valid content!")
    else:
        # using filter return the response
        shops = Shop.objects.all()
        bikes = Bike.objects.all()

        # to find out the busy bikes
        busy_bike_order_ids = []
        orders = Order.objects.exclude(time_from__lt=time_to, time_to__gt=time_from)
        for order in orders:
            order_bike_types = (bike.type for bike in order.bikes.all())
            if '1' in order_bike_types:
                pass
            if '2' in order_bike_types:
                pass
            if '3' in order_bike_types:
                pass

        # logging.debug("REST.readShops: shops: {}".format(shops))
        serializer = ShopSerializer(data=shops, many=True)
        if serializer.is_valid():
            return bad_request(serializer.errors)
        return Response(serializer.data)


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
        "bikes": <[int]>,
        "time_from": <str(date)>,
        "time_to": <str(date)>
    }
    """
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        # to return the response with counted invoice
        order = Order.objects.get(pk=serializer.data['id'])
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    return bad_request(serializer.errors)
