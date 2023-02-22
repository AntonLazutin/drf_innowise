from django.db import models


class SupportResponse(models.Model):
    ticket = models.ForeignKey('tickets.Ticket', related_name='responses', on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    date_responded = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.text[:20]}..."