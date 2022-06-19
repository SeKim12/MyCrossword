from rest_framework import serializers
from .models import ButtonCount


class ButtonCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ButtonCount
        fields = ('id', 'frequency', 'pressed')
