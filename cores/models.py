from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Config(models.Model):
    key = models.CharField(_('key'), max_length=255, blank=False, null=False, unique=True)
    value = models.TextField(_('value'))
    description = models.TextField(_('description'), null=True, blank=True)

    class Meta:
        verbose_name = _('config')
        verbose_name_plural = _('configs')

    def __str__(self):
        return "{}: {}".format(self.key, self.value)

    @staticmethod
    def get_by_key(key):
        try:
            return Config.objects.get(key=key)
        except Config.DoesNotExist:
            return None
