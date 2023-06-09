# Generated by Django 4.2.1 on 2023-06-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_qty', models.FloatField(default=0)),
                ('sale_qty', models.FloatField(default=0)),
                ('total_balace_qty', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('purchase', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.purchase')),
                ('sale', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.sale')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
    ]
