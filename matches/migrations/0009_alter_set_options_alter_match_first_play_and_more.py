# Generated by Django 5.1 on 2024-08-29 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0008_set_winner'),
        ('users', '0002_remove_user_name_alter_user_email_player'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='set',
            options={'verbose_name': 'Сет', 'verbose_name_plural': 'Сеты'},
        ),
        migrations.AlterField(
            model_name='match',
            name='first_play',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_plays', to='users.player'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game1_score1',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 1-й игры команды 1'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game1_score2',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 1-й игры команды 2'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game2_score1',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 2-й игры команды 1'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game2_score2',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 2-й игры команды 2'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game3_score1',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 3-й игры команды 1'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game3_score2',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 3-й игры команды 2'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game4_score1',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 4-й игры команды 1'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game4_score2',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 4-й игры команды 2'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game5_score1',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 5-й игры команды 1'),
        ),
        migrations.AlterField(
            model_name='set',
            name='game5_score2',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=None, null=True, verbose_name='Счет 5-й игры команды 2'),
        ),
        migrations.AlterField(
            model_name='set',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='matches.match', verbose_name='Матч'),
        ),
        migrations.AlterField(
            model_name='set',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.player', verbose_name='Победитель'),
        ),
    ]
