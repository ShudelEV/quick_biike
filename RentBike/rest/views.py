from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RentBike.models import Shop
from .serializers import ShopSerializer


@api_view(['POST'])
def readShops(request):
    """
        API endpoint that return set of shops using filter:
    {
         "filter":{
             "order": {
                 "from": "<str(date)>",
                 "to": "<str(date)"
             },
             "bike": {
                 "typeIds": "<[int]>",
                 "count": "<int>"
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