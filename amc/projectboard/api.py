from rest_framework.generics import ListAPIView
from rest_framework.decorators import detail_route

from .serializers import qpSerializer
from .models import qp

class qpApi(ListAPIView):
    queryset = qp.objects.all()
    serializer_class = qpSerializer