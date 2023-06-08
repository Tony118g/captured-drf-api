from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo


class Comment(models.Model):
    """
    The model for comments, related to User and Photo.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders comments by date they were created
        from newest to oldest.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the content of the comment.
        """
        return self.content
