from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from RentBike.models import Shop, Order, Bike
from .serializers import ShopSerializer, BikeSerializer, OrderSerializer, ShopWithBikesSerializer
from django.views.decorators.csrf import csrf_protect
from copy import copy
from collections import OrderedDict
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


# find out busy bikes
def get_busy_bikes(free_from, free_to):
    busy_bike_ids = []

    if free_from and free_to:
        for order in Order.objects.exclude(time_from__gte=free_to).exclude(time_to__lte=free_from):
            busy_bike_ids += [bike.id for bike in order.bikes.all()]
    elif free_from and not free_to:
        for order in Order.objects.exclude(time_to__lte=free_from):
            busy_bike_ids += [bike.id for bike in order.bikes.all()]

    # logging.debug("REST/Busy bike ids: {}".format(busy_bike_ids))

    return busy_bike_ids

@api_view(['POST'])
@permission_classes((AllowAny, ))
def read_shops(request):
    """
        API endpoint that return set of shops using filter:
    {
        "bike_is_free": {
            "from": <str(date)>,
            "to": <str(date)>
            },
        "bikes: [
           { "type": <int>, "quantity": <int> },
           { "type": <int>, "quantity": <int> },
           ...
        ]
    } }
    """
    # logging.debug("REST.readShops/Form: {}".format(request.data))

    filter_data = request.data

    try:
        free_from = filter_data['bike_is_free']['from']
        free_to = filter_data['bike_is_free']['to']
        bikes = filter_data['bikes']
        # count types of bikes
        order_type_count = {}
        if bikes:
            order_type_count = {bike['type']: bike['quantity'] for bike in bikes}

        # logging.debug("REST.readShops/Type_count: {}".format(type_count))

    except KeyError:
        return bad_request("detail: Not valid content!")

    # using filter return the response
    else:
        busy_bike_ids = get_busy_bikes(free_from, free_to)

        # to find out shops that have relevant bikes
        shop_ids = []
        if bikes:
            for shop in Shop.objects.select_related('bikes'):
                shop_type_count = order_type_count.copy()

                for bike in shop.bikes.exclude(pk__in=busy_bike_ids):
                    b_type = int(bike.type)
                    if b_type in list(order_type_count.keys()):
                        shop_type_count[b_type] -= 1

                # check: does this shop have relevant bikes?
                comp = True
                for val in shop_type_count.values():
                    if val > 0:
                        comp = False
                if comp:
                    shop_ids.append(shop.id)
        else:
            shop_ids = [shop.id for shop in Shop.objects.all()]

        # create the response "list of shops with a filtered bikes set"
        # work with serializers that to don't update shop.bikes in db
        shops_qset = Shop.objects.filter(pk__in=shop_ids)
        shops_ser = ShopSerializer(shops_qset, many=True)
        for shop, sh in zip(shops_qset, shops_ser.data):
            # get free bikes set for a shop
            bikes = shop.bikes.exclude(pk__in=busy_bike_ids)
            bikes_ser_data = BikeSerializer(bikes, many=True).data
            # add a free bikes set to a shop
            sh.update([('bikes', bikes_ser_data)])

        return Response({"shops": shops_ser.data})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def read_bikes(request):
    """
        API endpoint that return set of bikes using filter:
    {
        "bike_is_free": {
            "from": <str(date)>,
            "to": <str(date)>
            },
        "bikes: [
           { "type": <int>, "quantity": <int> },
           { "type": <int>, "quantity": <int> },
           ...
        ],
        ?"shop": { "id": <[int]> }
    } }
    """
    # logging.debug("REST.readBikes/Form: {}".format(request.data))

    filter_data = request.data

    try:
        free_from = filter_data['bike_is_free']['from']
        free_to = filter_data['bike_is_free']['to']
        bikes = filter_data['bikes']
        # count types of bikes
        bike_types = []
        if bikes:
            bike_types = [str(bike['type']) for bike in bikes]

        shop_ids = filter_data['shop']['id']

    except KeyError:
        return bad_request("detail: Not valid content!")

    # using filter return the response
    else:
        busy_bike_ids = get_busy_bikes(free_from, free_to)
        shops = Shop.objects.filter(pk__in=shop_ids) if shop_ids else Shop.objects.all()

        if bike_types:
            bikes_query = Bike.objects\
                .exclude(pk__in=busy_bike_ids)\
                .filter(shop__in=shops)\
                .filter(type__in=bike_types)
        else:
            bikes_query = Bike.objects\
                .exclude(pk__in=busy_bike_ids)\
                .filter(shop__in=shops)

        return Response({"bikes": BikeSerializer(bikes_query, many=True).data})


@api_view(['POST'])
def create_order(request):
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
