from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    STATUS_CHOICES = (
        ('ava', _('available')),
        ('not', _('not_available')),
    )
    title = models.CharField(max_length=500, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True, verbose_name=_('slug'))
    short_description = RichTextField(verbose_name=_('short description'), blank=True)
    description = RichTextField(verbose_name=_('description'), blank=True)
    price = models.PositiveIntegerField(verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava', verbose_name=_('status'))
    image = models.ImageField(upload_to='covers/', verbose_name=_('image'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-datetime_created']

    def cover_img(self):
        return format_html("<img width=60 src='{}'>".format(self.image.url))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:details_view', args=[self.slug])
