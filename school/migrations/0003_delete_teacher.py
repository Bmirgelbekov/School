# Generated by Django 4.2.2 on 2023-06-27 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teacher_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]