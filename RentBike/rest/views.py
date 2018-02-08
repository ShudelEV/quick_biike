from rest_framework import viewsets, status
from rest_framework.decorators import api_view, list_route, detail_route
from rest_framework.response import Response
from RentBike.models import Shop, Order, Bike
from .serializers import ShopSerializer, BikeSerializer, OrderSerializer

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


class BikeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that return set of bikes
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that return set of orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['POST'])
def readShops(request):
    """
        API endpoint that return set of shops using filter:
    { "filter":{
             "bike_is_free": {
                 "from": <str(date)>,
                 "to": <str(date)> },
             "bike_count": {
                 "type1": <int>,
                 "type2": <int>,
                 "type3": <int> }
    } } }
    """
    try:
        filter_data = request.data['filter']

        logging.debug("REST.readShops: filter: {}".format(filter_data))

        free_from = filter_data['bike_is_free']['from']
        free_to = filter_data['bike_is_free']['to']
        type1_count = filter_data['bike_count']['type1']
        type2_count = filter_data['bike_count']['type2']
        type3_count = filter_data['bike_count']['type3']

    except KeyError:
        return bad_request("detail: Not valid content!")

    # using filter return the response
    else:
        # to find out the busy bikes
        busy_bike_ids = []
        for order in Order.objects.exclude(time_from__gte=free_to).exclude(time_to__lte=free_from):
            busy_bike_ids += [bike.id for bike in order.bikes.all()]
        busy_bike_ids = set(busy_bike_ids)

        # to find out shops that have relevant bikes
        shop_ids = []
        for shop in Shop.objects.all():
            # count of type bikes
            type_count = {'1': 0, '2': 0, '3': 0}
            for bike in shop.bike_set.exclude(pk__in=busy_bike_ids):
                if bike.type == '1':
                    type_count['1'] += 1
                elif bike.type == '2':
                    type_count['2'] += 1
                elif bike.type == '3':
                    type_count['3'] += 1
            # to check: does the shop have relevant bikes?
            if type_count['1'] >= type1_count \
                    and type_count['2'] >= type2_count \
                    and type_count['3'] >= type3_count:
                shop_ids.append(shop.id)

        # logging.debug("REST.readShops: Order.shops.ids: {}".format(shop_ids))

        return Response({"shops": shop_ids})


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
