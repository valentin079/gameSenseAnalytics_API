# Generated by Django 4.2.5 on 2023-11-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo_bet', '0003_jogo_corneraway_jogo_cornerhome'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='date_game',
            field=models.DateTimeField(default='2023-11-21 09:13:30'),
        ),
    ]
