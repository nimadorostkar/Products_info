from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class AdvertiseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('img','name')
    search_fields = ['name',]
admin.site.register(models.Advertise, AdvertiseAdmin)