# Generated by Django 5.0.7 on 2024-10-10 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0016_rename_password_reset_used_employee_reset_password_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='reset_password_flag',
        ),
    ]
