# Generated by Django 5.1 on 2024-08-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_alter_match_score1_alter_match_score2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
