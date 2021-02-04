from django.db import models

from django_hello.backend import AzurePublicStorage


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class FileUpload(models.Model):
    private_upload = models.FileField(null=True, blank=True)
    public_upload = models.FileField(storage=AzurePublicStorage, null=True, blank=True)
