from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class TicketSupportSerializer(ModelSerializer):
    """
    Serializer of Ticket model for staff user
    # """
    # author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = 'tickets.Ticket'
        fields = '__all__'
