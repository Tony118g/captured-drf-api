from django.db import models
from django.contrib.auth.models import User


class Tour(models.Model):
    """
    The model for tours.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.DecimalField(
        blank=True, max_digits=8, decimal_places=2, default='00.00'
        )
    guide = models.CharField(
        max_length=100,
        blank=True,
        default='currently unknown'
        )
    start_date = models.DateField()
    end_date = models.DateField()
    booking_means = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders tours by date they were created
        from newest to oldest.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the id and title of the tour.
        """
        return f'{self.id} {self.title}'
