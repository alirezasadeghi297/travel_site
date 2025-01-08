from django.contrib import admin
from . import models

class Postadmin(admin.ModelAdmin):
    list_display = ['title','counted_views','status','published_date','created_date']
admin.site.register(models.Post, Postadmin)

# Register your models here.
