# Generated by Django 5.1.1 on 2024-09-29 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customproductsmodel',
            name='description',
            field=models.CharField(blank=True, null=True),
        ),
    ]
