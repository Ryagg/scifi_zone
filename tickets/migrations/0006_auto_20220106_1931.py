# Generated by Django 3.2.9 on 2022-01-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='included',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='star',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticketholder_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
