from rest_framework import serializers

from .models import qp

class qpSerializer(serializers.ModelSerializer):

    class Meta:
        model=qp
        fields = '__all__'
