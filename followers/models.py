from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    The model for followers, related to User
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
        )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders followers by date they were created
        from newest to oldest and ensures a user
        can't follow the same user more than once
        """
        unique_together = ['owner', 'followed']
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string with the owner and followed fields
        """
        return f'{self.owner} {self.followed}'
