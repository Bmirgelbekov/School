# Generated by Django 4.2.2 on 2023-06-28 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_managers_remove_teacher_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
    ]
