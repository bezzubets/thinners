# Generated by Django 3.2.7 on 2021-09-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210921_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ukr_thinners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Здесь пишем наименование растворителя', max_length=30, verbose_name='Наименование')),
                ('purpose', models.CharField(help_text='Здесь пишем назначение растворителя', max_length=50, verbose_name='Назначение')),
                ('price', models.CharField(help_text='Здесь пишем цену растворителя', max_length=20, verbose_name='Цена')),
                ('currency', models.CharField(help_text='Здесь пишем валюту растворителя', max_length=20, verbose_name='Валюта')),
                ('description', models.TextField(help_text='Здесь пишем комментарий', verbose_name='Комментарий')),
                ('country', models.CharField(help_text='Здесь пишем страну производства растворителя', max_length=50, verbose_name='Страна')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.im')),
            ],
        ),
    ]
