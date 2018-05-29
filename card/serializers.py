from card.models import Cards
from rest_framework import serializers


class CheckInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ('card_no',)
        lookup_field = 'card_no'
        extra_kwargs = {
            'url': {'lookup_field': 'card_no'}
        }
