# Generated by Django 4.2 on 2023-11-04 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_remove_byte_memberlikes_remove_byte_studentlikes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='byte',
            name='owner',
        ),
    ]
