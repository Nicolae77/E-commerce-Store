# Generated by Django 4.0.4 on 2022-06-14 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_date',
            new_name='created_date',
        ),
    ]