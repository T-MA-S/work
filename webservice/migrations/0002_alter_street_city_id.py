# Generated by Django 4.0.3 on 2022-04-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.city'),
        ),
    ]
