# Generated by Django 3.2 on 2025-03-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.TextField()),
                ('prod_description', models.TextField()),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.TextField()),
            ],
        ),
    ]
