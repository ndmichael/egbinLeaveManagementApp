# Generated by Django 3.1.7 on 2021-04-03 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0004_auto_20210403_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='leave_balance',
            new_name='final_balance_old',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='leave_balance_old',
            new_name='initial_balance',
        ),
    ]
