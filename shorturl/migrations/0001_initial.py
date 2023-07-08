# Generated by Django 4.2.3 on 2023-07-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_acceseed', models.DateTimeField(blank=True, null=True)),
                ('time_followed', models.PositiveIntegerField(default=0)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=10, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
