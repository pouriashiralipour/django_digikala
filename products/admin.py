from django.contrib import admin, messages
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext, gettext_lazy as _, ngettext
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

from .models import Products


@admin.register(Products)
class ProductAdmin(ModelAdminJalaliMixin, ImportExportModelAdmin):
    list_display = ['title', 'cover_img', 'slug', 'category_display', 'price', 'status', 'active', 'datetime_created']
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_not_available', 'make_available', 'make_active', 'make_de_active']

    def category_display(self, obj):
        return " ، ".join([category.title for category in obj.category.all()])

    category_display.short_description = _("categories")

    @admin.action(description=_('Selected products are not available'))
    def make_not_available(self, request, queryset):
        updated = queryset.update(status='not')
        self.message_user(request, ngettext(
            _('%d story was successfully marked as not available.'),
            _('%d stories were successfully marked as not available.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are active'))
    def make_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as activated.'),
            _('%d stories were successfully marked as activated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are de_active'))
    def make_de_active(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as deactivated.'),
            _('%d stories were successfully marked as deactivated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are available'))
    def make_available(self, request, queryset):
        updated = queryset.update(status='ava')
        self.message_user(request, ngettext(
            _('%d story was successfully marked as available.'),
            _('%d stories were successfully marked as available.'),
            updated,
        ) % updated, messages.SUCCESS)

