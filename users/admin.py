import codecs
import csv

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.utils.translation import gettext as _
from users.models import CustomUser, TypeActivity, Wishlist

def export_users_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=users_export.csv'

    # Use the codecs module for explicit encoding
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response, quoting=csv.QUOTE_ALL)

    writer.writerow([
        smart_str(_('ID')),
        smart_str(_('Username')),
        smart_str(_('First Name')),
        smart_str(_('Last Name')),
        smart_str(_('City')),
        # Add more fields as needed
    ])

    for user in queryset:
        writer.writerow([
            smart_str(user.id),
            smart_str(user.username),
            smart_str(user.first_name),
            smart_str(user.last_name),
            smart_str(user.city),
            # Add more fields as needed
        ])

    return response

export_users_to_excel.short_description = _("Экспорт в Excel")

class CustomUserAdmin(DefaultUserAdmin):
    actions = [export_users_to_excel]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'city', 'telegram', 'insta', 'type_activity', 'status', 'rebill_id', 'created_pay', 'extension', 'save_hashtag')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TypeActivity)
admin.site.register(Wishlist)