# Generated by Django 3.1.14 on 2023-09-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0004_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='sheet_name',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
