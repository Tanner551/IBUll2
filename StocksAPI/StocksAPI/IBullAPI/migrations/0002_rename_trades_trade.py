# Generated by Django 3.2.9 on 2021-11-16 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IBullAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trades',
            new_name='Trade',
        ),
    ]