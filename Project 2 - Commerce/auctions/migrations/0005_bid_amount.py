# Generated by Django 3.1.1 on 2020-09-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200923_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
