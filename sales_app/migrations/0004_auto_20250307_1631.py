# Generated by Django 3.2 on 2025-03-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0003_alter_orders_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_items',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_items',
            field=models.ManyToManyField(related_name='orders', to='sales_app.Products'),
        ),
    ]
