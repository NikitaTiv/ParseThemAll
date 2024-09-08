from django.db import models

from images.utils import get_directory_path


class Image(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 1
        UPLOADED = 2
        PARSED = 3
    status = models.PositiveSmallIntegerField(choices=Status, default=Status.DRAFT)
    file_path = models.ImageField(upload_to=get_directory_path)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
