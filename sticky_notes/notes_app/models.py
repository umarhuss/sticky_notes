from django.db import models
from django.contrib.auth.models import User  # Import User model


class StickyNote(models.Model):
    # Associate with user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
