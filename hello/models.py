from django.db import models

from django_hello.backend import AzurePublicStorage

class FileUpload(models.Model):
    private_upload = models.FileField(null=True, blank=True)
    public_upload = models.FileField(storage=AzurePublicStorage, null=True, blank=True)
