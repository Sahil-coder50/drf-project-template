from .audit_mixin import AuditMixin
from .time_mixin import TimeMixin
from .soft_delete import SoftDeleteMixin

class BaseMixin(AuditMixin, TimeMixin, SoftDeleteMixin):

    class Meta:
        abstract = True
