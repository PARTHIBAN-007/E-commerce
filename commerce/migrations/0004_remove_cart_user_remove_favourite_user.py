# Generated by Django 4.2.9 on 2024-02-02 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
    ]
