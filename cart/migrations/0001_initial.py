# Generated by Django 4.1.5 on 2023-01-16 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_product_name', models.CharField(max_length=100)),
                ('cart_product_desc', models.TextField()),
                ('cart_prod_quantity', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('cart_product_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_product_discount', models.FloatField(max_length=4)),
                ('cart_prod_sell_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_prod_net_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_prod_deli_chrg', models.DecimalField(decimal_places=2, default=0, max_digits=1000, null=True)),
                ('cart_prod_total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('order_completed', models.BooleanField(default=False)),
                ('cart_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customermodel')),
                ('order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.ordermodel')),
            ],
        ),
    ]
