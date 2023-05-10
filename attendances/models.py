from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour


class Attendance(models.Model):
    """
    The model for attendances, related to User and Tour
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='attendances'
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders attendances by date they were created
        from newest to oldest and ensures a user
        can't mark the same tour as attending twice.
        """
        unique_together = ['owner', 'tour']
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the owner and tour of the attendance
        """
        return f'{self.owner} {self.tour}'
