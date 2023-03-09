from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    STATUS_CHOICES = (
        ('ava', _('available')),
        ('not', _('not_available')),
    )
    title = models.CharField(max_length=500, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True, verbose_name=_('slug'))
    description = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava', verbose_name=_('status'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-datetime_created']