# Generated by Django 4.2.2 on 2023-06-12 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choice',
        ),
    ]
