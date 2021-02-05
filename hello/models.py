from django.db import models

from django_hello.backend import PrivateStorage, PublicStorage

class FileUpload(models.Model):
    private_upload = models.FileField(storage=PrivateStorage, null=True, blank=True)
    public_upload = models.FileField(storage=PublicStorage, null=True, blank=True)
