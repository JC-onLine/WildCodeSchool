# Generated by Django 3.1.2 on 2021-01-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautes', '0004_auto_20210103_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applisettings',
            name='columns_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='applisettings',
            name='members_maxi',
            field=models.IntegerField(unique=True),
        ),
    ]
