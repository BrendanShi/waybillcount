# Generated by Django 3.0.8 on 2020-07-15 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '账号管理', 'verbose_name_plural': '账号管理'},
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('manager', '管理员'), ('picker', '接单员'), ('driver', '司机')], max_length=20, verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]