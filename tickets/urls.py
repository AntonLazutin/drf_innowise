from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TicketUserViewSet

app_name = "tickets"

router = SimpleRouter()
router.register('tickets', TicketUserViewSet, basename='tickets')

urlpatterns = router.urls