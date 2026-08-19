from django.db import models

class SoftDeleteMixin(models.Model):

    is_deleted = models.BooleanField(is_deleted=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True