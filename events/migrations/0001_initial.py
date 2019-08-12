# Generated by Django 2.2.4 on 2019-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_text', models.CharField(max_length=100)),
                ('event_owner', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField(verbose_name='Event date')),
                ('event_theme', models.CharField(default='Without theme', max_length=20)),
                ('event_city', models.CharField(max_length=30)),
                ('event_name', models.CharField(max_length=100)),
                ('event_address', models.CharField(max_length=100)),
            ],
        ),
    ]
