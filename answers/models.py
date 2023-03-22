from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    parent_ticket = models.ForeignKey('tickets.Ticket', related_name='answers', on_delete=models.CASCADE)
    parent_answer = models.ForeignKey('self', related_name='answers', on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:30]}..."
