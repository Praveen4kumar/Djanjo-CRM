# Generated by Django 5.0.2 on 2024-02-18 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
