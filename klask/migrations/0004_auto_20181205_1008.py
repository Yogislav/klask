# Generated by Django 2.1.4 on 2018-12-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klask', '0003_auto_20181205_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.IntegerField(default=1000, verbose_name='Ranking'),
        ),
        migrations.AlterField(
            model_name='playerhistory',
            name='rating',
            field=models.IntegerField(verbose_name='Ranking'),
        ),
    ]
