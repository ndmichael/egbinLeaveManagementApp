# Generated by Django 3.1.7 on 2021-04-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0002_auto_20210403_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='date_approved',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
