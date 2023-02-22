from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TicketViewSet

app_name = "tickets"

router = SimpleRouter()
router.register('tickets', TicketViewSet, basename='tickets')

urlpatterns = router.urls