# Generated by Django 4.2 on 2023-05-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0013_amount_category_coverage_category_option_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.amount'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('Ck', 'Cake'), ('Cup', 'Cupcake'), ('Cp', 'Cakepop'), ('Co', 'Cookie')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='coverage',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.coverage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='flavour',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.flavours'),
        ),
        migrations.AlterField(
            model_name='item',
            name='option',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.option'),
        ),
        migrations.AlterField(
            model_name='item',
            name='topping',
            field=models.ManyToManyField(blank=True, null=True, to='Cupcakaya.toppings'),
        ),
    ]
