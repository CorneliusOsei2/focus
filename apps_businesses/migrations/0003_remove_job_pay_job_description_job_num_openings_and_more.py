# Generated by Django 4.0.4 on 2022-08-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_businesses', '0002_team_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='pay',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='job',
            name='num_openings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]