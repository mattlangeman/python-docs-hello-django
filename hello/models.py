from django.db import models

from django_hello.backend import PrivateStorage, PublicStorage

class FileUpload(models.Model):
    private_upload = models.FileField(upload_to='private_uploads', storage=PrivateStorage, null=True, blank=True)
    public_upload = models.FileField(upload_to='public_uploads', storage=PublicStorage, null=True, blank=True)
