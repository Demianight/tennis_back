# Generated by Django 5.1 on 2024-08-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
