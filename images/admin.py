from django.contrib import admin

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ["filename", 'status', 'created']


admin.site.register(Image)
