# Generated by Django 4.2 on 2023-04-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SineData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_val', models.DecimalField(decimal_places=20, max_digits=30)),
                ('label', models.TimeField(auto_now=True)),
            ],
            options={
                'db_table': 'dashboard_sinedata',
                'managed': False,
            },
        ),
    ]
