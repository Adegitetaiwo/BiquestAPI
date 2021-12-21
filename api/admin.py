from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import QuizArchive
from django.http import HttpResponse
import csv

# Register your models here.
admin.site.site_header = 'Biquest'
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export selected Quiz Archive as csv"



@admin.register(QuizArchive)
class QuizArchiveAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['question']
    actions = ['export_as_csv']

    
