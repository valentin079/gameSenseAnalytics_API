# Generated by Django 4.2.5 on 2023-11-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo_bet', '0004_jogo_date_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='date_game',
            field=models.DateTimeField(default='2023-11-21'),
        ),
    ]