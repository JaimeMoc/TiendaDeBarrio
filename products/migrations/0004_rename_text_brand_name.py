# Generated by Django 5.1.4 on 2025-01-07 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='text',
            new_name='name',
        ),
    ]