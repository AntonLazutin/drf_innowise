from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .permissions import OwnerPermission
from .serializers import TicketSerializer
from .models import Ticket


class TicketUserViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (OwnerPermission,)