# Generated by Django 3.1.3 on 2024-02-16 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_dairy_dataset_food_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dairy',
            new_name='diary',
        ),
    ]
