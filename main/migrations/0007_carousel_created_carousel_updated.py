# Generated by Django 4.0.5 on 2022-06-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
