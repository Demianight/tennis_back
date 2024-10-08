# Generated by Django 5.1 on 2024-08-29 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0009_alter_set_options_alter_match_first_play_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='game1_score1',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game1_score2',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game2_score1',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game2_score2',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game3_score1',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game3_score2',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game4_score1',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game4_score2',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game5_score1',
        ),
        migrations.RemoveField(
            model_name='set',
            name='game5_score2',
        ),
        migrations.AddField(
            model_name='set',
            name='number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('score1', models.PositiveIntegerField(choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=0)),
                ('score2', models.PositiveIntegerField(choices=[(0, 0), (15, 15), (30, 30), (40, 40)], default=0)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='matches.set', verbose_name='Сет')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
