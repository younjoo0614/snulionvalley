# Generated by Django 3.0.8 on 2020-07-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200729_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='already_read',
            field=models.IntegerField(blank=True),
        ),
    ]
