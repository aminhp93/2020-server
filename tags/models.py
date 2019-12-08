from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=30, unique=True)

    def __str__(self):
        return self.name
