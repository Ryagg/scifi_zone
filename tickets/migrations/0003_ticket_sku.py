# Generated by Django 3.2.9 on 2022-01-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20220104_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='sku',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]