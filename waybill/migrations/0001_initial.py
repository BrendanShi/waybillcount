# Generated by Django 3.0.8 on 2020-07-13 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='顾客名称')),
            ],
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='公司名称')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=20, verbose_name='车牌号')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部门名称')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='waybill.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(max_length=50, verbose_name='发货地')),
                ('receipt', models.CharField(max_length=50, verbose_name='收货地')),
                ('items', models.CharField(max_length=20, verbose_name='运货清单')),
                ('number', models.CharField(max_length=20, verbose_name='运单号')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_checklists', to='waybill.Department')),
                ('logistics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_checklists', to='waybill.Logistics')),
            ],
        ),
    ]
