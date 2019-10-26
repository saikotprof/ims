from django.contrib import admin
from .models import Brand, Device, Apple, Samsung, Xiaomi
from import_export.admin import ImportExportModelAdmin

admin.site.register(Brand)
admin.site.register(Device)

@admin.register(Apple, Samsung, Xiaomi)
class ViewAdmin(ImportExportModelAdmin):
	exclude = ('id', )
