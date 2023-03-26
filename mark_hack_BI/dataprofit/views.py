from rest_framework import viewsets

from .models import Defect, ABC_NEW, Price_min_max
from .serializers import DefectSerializer, ABCSerializer, Price_min_maxSerializer


class DefectViewset(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer


class ABCViewset(viewsets.ModelViewSet):
    queryset = ABC_NEW.objects.all()
    serializer_class = ABCSerializer

class Price_min_maxViewset(viewsets.ModelViewSet):
    queryset = Price_min_max.objects.all()
    serializer_class = Price_min_maxSerializer