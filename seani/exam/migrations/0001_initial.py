# Generated by Django 5.0.2 on 2024-02-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(max_length=2, verbose_name='Etapa')),
                ('application_date', models.DateField(verbose_name='Fecha de aplicación')),
            ],
            options={
                'verbose_name': 'etapa',
                'verbose_name_plural': 'etapas',
            },
        ),
    ]
