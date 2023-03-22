from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .permissions import OwnerOrReadOnly
from .serializers import TicketSerializer
from .models import Ticket


class TicketUserViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (OwnerOrReadOnly,)
    #http_method_names = ['get', 'post', 'put', 'patch']

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)