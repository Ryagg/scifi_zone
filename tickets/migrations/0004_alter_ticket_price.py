# Generated by Django 3.2.9 on 2022-01-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
