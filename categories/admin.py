from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.utils.translation import gettext, gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


from .models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdminJalaliMixin, ImportExportModelAdmin):
    list_display = ['title', 'slug', 'parent', 'active', 'datetime_created']
    search_fields = ('title', 'parent',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_active', 'make_not_active', ]

    @admin.action(description=_('Selected categories are not active'))
    def make_not_active(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as not activated.'),
            _('%d stories were successfully marked as not activated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected categories are active'))
    def make_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as activated.'),
            _('%d stories were successfully marked as activated.'),
            updated,
        ) % updated, messages.SUCCESS)
