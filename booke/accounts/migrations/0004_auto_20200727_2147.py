# Generated by Django 3.0.8 on 2020-07-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_already_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='goal',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
