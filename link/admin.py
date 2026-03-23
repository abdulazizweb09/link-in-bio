from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    list_display=['name','slug','img','tg','tg_akk','insta','youtube','tiktok','link','github']