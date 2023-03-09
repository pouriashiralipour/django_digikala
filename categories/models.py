import random

from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.translation import gettext, gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self',
                               default=None,
                               null=True, blank=True,
                               verbose_name=_('parent'),
                               on_delete=models.SET_NULL,
                               related_name='child', )
    title = models.CharField(max_length=300, verbose_name=_('title'))
    slug = models.SlugField(max_length=400, verbose_name=_('slug'), unique=True, allow_unicode=True)
    # image = models.ImageField(upload_to='category_img/', verbose_name=_('image'), blank=True, null=True)
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'), )
    active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title

    # def cover_img(self):
    #     return format_html("<img width=60 src='{}'>".format(self.image.url))

    # cover_img.short_description = _('image')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def products_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    # print(sender, instance)
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(products_pre_save, sender=Category)


def products_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(products_post_save, sender=Category)

