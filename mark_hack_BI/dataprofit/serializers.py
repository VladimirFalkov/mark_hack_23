from rest_framework import serializers

from .models import Defect, ABC_NEW, Price_min_max


class DefectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Defect
        fields = "__all__"


class ABCSerializer(serializers.ModelSerializer):

    class Meta:
        model = ABC_NEW
        fields = "__all__"

class Price_min_maxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price_min_max
        fields = "__all__"