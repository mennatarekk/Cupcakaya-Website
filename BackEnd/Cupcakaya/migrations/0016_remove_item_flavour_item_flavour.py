# Generated by Django 4.2 on 2023-05-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0015_remove_item_flavour_item_flavour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='flavour',
        ),
        migrations.AddField(
            model_name='item',
            name='flavour',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.flavours'),
        ),
    ]
