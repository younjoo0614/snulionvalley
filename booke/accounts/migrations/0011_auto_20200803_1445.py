# Generated by Django 3.0.8 on 2020-08-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_merge_20200803_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='already_read',
        ),
        migrations.AddField(
            model_name='profile',
            name='already',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]