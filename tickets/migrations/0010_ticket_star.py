# Generated by Django 3.2.9 on 2022-01-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20220107_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='star',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
