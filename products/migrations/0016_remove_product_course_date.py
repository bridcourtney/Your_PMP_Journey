# Generated by Django 3.1.5 on 2021-02-22 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210222_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='course_date',
        ),
    ]
