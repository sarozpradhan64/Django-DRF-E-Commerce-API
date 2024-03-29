# Generated by Django 4.0.5 on 2022-06-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_created_product_publish_product_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='carousel/')),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='products/thumbnail'),
        ),
    ]
