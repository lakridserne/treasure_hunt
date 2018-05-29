from django.conf.urls import url, include
from rest_framework import routers
from card.views import CheckInView

router = routers.SimpleRouter()
router.register(r'checkin', CheckInView)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls
