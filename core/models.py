from django.db import models
from django.utils.translation import gettext_lazy as _

from core import consts


class BaseModel(models.Model):
    """Basic entity model. Implements fields: name, created_at."""

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=consts.NAME_MAX_LENGTH,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
