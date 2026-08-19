from django.db import models

class AuditMixin(models.Model):

    created_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    updated_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    class Meta:
        abstract = True
