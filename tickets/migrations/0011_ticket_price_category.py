# Generated by Django 3.2.9 on 2022-01-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_ticket_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price_category',
            field=models.CharField(default='B', max_length=1),
        ),
    ]
