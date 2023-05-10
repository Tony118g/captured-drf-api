from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo


class Like(models.Model):
    """
    The model for likes, related to User and Photo
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='likes'
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders likes by date they were created
        from newest to oldest and ensures a user
        can't like the same photo twice.
        """
        unique_together = ['owner', 'photo']
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the owner and photo of the like
        """
        return f'{self.owner} {self.photo}'
