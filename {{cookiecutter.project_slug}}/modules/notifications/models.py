from django.db import models

# Create your models here.

class Notification(models.Model):
    message = models.TextField(null=True, blank=True)

    owner_id = models.IntegerField(verbose_name="Notification Creator", null=True, blank=True)

    seen = models.BooleanField(default=False)
    linked_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    updated_by_id = models.IntegerField(verbose_name="Notification Modifier", null=True, blank=True)

    def __str__(self):
        return str(self.message)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
