from django.contrib import admin
from . import models

class Postadmin(admin.ModelAdmin):
    list_display = ['title','author','counted_views','status','published_date','created_date']
    list_filter=['published_date','status']
    search_fields=['title','content']

admin.site.register(models.Category)
admin.site.register(models.Post, Postadmin)


# Register your models here.
