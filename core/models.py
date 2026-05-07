from django.db import models
from django.contrib.auth.models import User

class Hack(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title', 'user')
