# Generated by Django 4.2.20 on 2025-03-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_technical_specification_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
