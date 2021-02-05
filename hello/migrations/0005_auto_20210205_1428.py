# Generated by Django 3.1 on 2021-02-05 14:28

from django.db import migrations, models
import django_hello.backend


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20210204_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='public_upload',
            field=models.FileField(blank=True, null=True, storage=django_hello.backend.AzurePublicStorage(), upload_to=''),
        ),
    ]
