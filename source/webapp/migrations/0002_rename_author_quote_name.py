# Generated by Django 4.0.3 on 2022-04-01 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author',
            new_name='name',
        ),
    ]
