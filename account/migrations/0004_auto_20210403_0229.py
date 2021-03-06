# Generated by Django 3.1.7 on 2021-04-03 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210402_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemanager',
            name='isLineManager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='line_manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.linemanager'),
        ),
    ]
