# Generated by Django 4.1.5 on 2023-01-16 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_alter_ordermodel_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
