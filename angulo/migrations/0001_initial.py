# Generated by Django 3.1.2 on 2021-01-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('angle', models.IntegerField()),
                ('date', models.DateField(default='2021-01-12')),
            ],
            options={
                'verbose_name': 'Angulo',
                'verbose_name_plural': 'Angulos',
            },
        ),
    ]
