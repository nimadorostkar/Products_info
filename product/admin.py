from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
admin.site.register(models.Category, CategoryAdmin)


class TypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
admin.site.register(models.Type, TypeAdmin)


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('img','name','barcode')
    search_fields = ['name','barcode']
    list_filter = ('category','type')
    raw_id_fields = ['category','type']
admin.site.register(models.Product, ProductAdmin)