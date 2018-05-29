from django.utils import timezone
from rest_framework import viewsets
from card.models import Teams, Cards, Posts
from card.serializers import CheckInSerializer


# Create your views here.
class CheckInView(viewsets.ReadOnlyModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CheckInSerializer
    lookup_field = 'card_no'

    def get_queryset(self):
        card_no = self.request.path.split('/')[2]
        pi = self.request.GET.get('pi', '')
        team = Teams.objects.get(cards__card_no=card_no)

        Posts.objects.create(
            team_id=team,
            time=timezone.now(),
            pi=pi
        )
        return self.queryset
