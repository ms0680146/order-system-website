# Generated by Django 2.1.9 on 2019-06-25 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custom_id',
            new_name='customer_id',
        ),
    ]