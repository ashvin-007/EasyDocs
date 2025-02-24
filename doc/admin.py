from django.contrib import admin
from .models import *

# Register your models here.

class adminDocUpload(admin.ModelAdmin):
    list_display=('title','doc','description')
    search_fields=('title',)
    
admin.site.register(DocUpload,adminDocUpload)

