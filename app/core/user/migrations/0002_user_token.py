# Generated by Django 3.0.4 on 2020-09-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]