# Generated by Django 2.2.3 on 2019-07-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]