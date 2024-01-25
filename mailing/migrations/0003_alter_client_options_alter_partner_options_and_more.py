# Generated by Django 5.0.1 on 2024-01-24 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_partner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',), 'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ('name_company',), 'verbose_name': 'партнер', 'verbose_name_plural': 'партнер'},
        ),
        migrations.CreateModel(
            name='ClientsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название списка')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='клиент для списка')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.partner')),
            ],
            options={
                'verbose_name': 'список клиентов для рассылки',
                'verbose_name_plural': 'список клиентов для рассылки',
                'ordering': ('name',),
            },
        ),
    ]