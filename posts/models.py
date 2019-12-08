from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from tags.models import Tag

class Post(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    content = models.TextField(_('content'), blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='post_creator'
    )
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('post')
        verbose_name_plural = _('posts')
    
    def __str__(self):
        return self.content_excerpt
    
    @property
    def content_excerpt(self, char_limit=120):
        """Returns an excerpt of the content for preview"""
        if len(self.content) > char_limit:
            return "{}...".format(self.content[:char_limti])
        return self.content



