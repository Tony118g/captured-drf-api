from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    The model for profiles.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_gaddut'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders profiles by date they were created
        from newest to oldest.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the owner of the profile.
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Creates a new user profile
    upon the creation of a new user.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
