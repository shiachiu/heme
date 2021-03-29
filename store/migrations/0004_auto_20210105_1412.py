# Generated by Django 3.0.8 on 2021-01-05 14:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210105_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retention',
            fields=[
                ('Period', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('Retention', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('Survival', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('Active_Customers', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('Active_Periods', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='o_id',
            new_name='o_ID',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='s_id',
            new_name='s_ID',
        ),
        migrations.RemoveField(
            model_name='material',
            name='m_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='o_data',
        ),
        migrations.RemoveField(
            model_name='product',
            name='m_ID',
        ),
        migrations.AddField(
            model_name='material',
            name='m_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 5, 14, 12, 2, 746115)),
        ),
        migrations.AddField(
            model_name='material',
            name='m_estdemand',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='material',
            name='m_estsupply',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='material',
            name='m_hcost',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='material',
            name='m_inventory',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='o_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='o_profit',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='p_cost',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='p_estdemand',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='p_estsupply',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='p_hcost',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='d_ID',
            field=models.CharField(default=0, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='d_name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='d_phone',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='material',
            name='m_name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='material',
            name='m_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='d_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Dealer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_amount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='p_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_inventory',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='s_name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='s_phone',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('U_quantity', models.DecimalField(decimal_places=0, max_digits=8)),
                ('m_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Material')),
                ('p_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_quantity', models.DecimalField(decimal_places=0, max_digits=8)),
                ('o_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
                ('p_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
    ]