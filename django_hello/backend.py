
from django.conf import settings
from storages.backends.azure_storage import AzureStorage


class AzurePrivateStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_STORAGE_KEY
    azure_container = settings.AZURE_MEDIA_CONTAINER
    expiration_secs = 60


class AzurePublicStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_STORAGE_KEY
    azure_container = settings.AZURE_STATIC_CONTAINER
    expiration_secs = None