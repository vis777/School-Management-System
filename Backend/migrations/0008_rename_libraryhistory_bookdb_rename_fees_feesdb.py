# Generated by Django 5.1.2 on 2024-10-24 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_remove_studentdb_age_remove_studentdb_phone_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LibraryHistory',
            new_name='BookDb',
        ),
        migrations.RenameModel(
            old_name='Fees',
            new_name='FeesDb',
        ),
    ]
