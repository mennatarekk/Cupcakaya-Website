# Generated by Django 4.2 on 2023-05-18 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0030_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
