from django.contrib import admin
from . import models

class Postadmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display = ['title','author','counted_views','status','published_date','created_date']
    list_filter=['published_date','status']
    search_fields=['title','content']
class Commentsadmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display = ['name','post','approved','created_date']
    list_filter=['created_date','approved']
    search_fields=['subject','post']

admin.site.register(models.Comments, Commentsadmin)
admin.site.register(models.Category)
admin.site.register(models.Post, Postadmin)


# Register your models here.
