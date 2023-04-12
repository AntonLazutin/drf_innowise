from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Ticket


class TicketSerializer(ModelSerializer):
    """
    Author sets to currently logged in user on POST request.
    But it's also visible on GET request
    """
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'
