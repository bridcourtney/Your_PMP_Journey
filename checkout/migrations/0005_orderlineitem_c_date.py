# Generated by Django 3.1.5 on 2021-02-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='c_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
