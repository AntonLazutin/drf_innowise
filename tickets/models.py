from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('PE', 'Pending'),
    ('FR', 'Frozen'),
    ('RE', 'Resolved'),
]


class Ticket(models.Model):
    author = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    status = models.CharField(default=STATUS_CHOICES[0], choices=STATUS_CHOICES, max_length=8)
    
    def __str__(self) -> str:
        return self.text