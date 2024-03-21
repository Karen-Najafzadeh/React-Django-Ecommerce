# Generated by Django 4.2.11 on 2024-03-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
