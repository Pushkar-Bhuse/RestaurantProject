# Generated by Django 2.2 on 2019-04-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_remove_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(null=True, to='delivery.OrderItem'),
        ),
    ]