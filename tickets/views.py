from rest_framework.viewsets import ModelViewSet

from .models import Ticket
from .permissions import OwnerOrReadOnly, IsSupport
from .serializers import TicketSerializer
#from ..support.serializers import TicketSupportSerializer

class TicketUserViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (OwnerOrReadOnly, IsSupport)

    # def get_serializer_class(self):

    #     if self.request.method in ('PUT', 'PATCH'): 
    #         pass
    #     else:
    #         pass
            
        # return super().get_serializer_class()
    #http_method_names = ['get', 'post', 'put', 'patch']

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)