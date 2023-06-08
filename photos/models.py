from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    """
    The model for photos, related to Owner/User.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    camera_used = models.CharField(
        default='unstated',
        max_length=100,
        blank=True
        )
    lense_used = models.CharField(
        default='unstated',
        max_length=100,
        blank=True
        )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_weccxi',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders photos by date they were created
        from newest to oldest.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the id and title of the photo.
        """
        return f'{self.id} {self.title}'
