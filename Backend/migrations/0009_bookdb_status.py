# Generated by Django 5.1.2 on 2024-10-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_rename_libraryhistory_bookdb_rename_fees_feesdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdb',
            name='status',
            field=models.CharField(choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')], default='borrowed', max_length=10),
        ),
    ]
