# Generated by Django 2.2 on 2019-04-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
