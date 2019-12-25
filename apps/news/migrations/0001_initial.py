# Generated by Django 2.2.6 on 2019-12-25 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('upcoming event', 'upcoming'), ('app update', 'app'), ('online competition', 'online'), ('past event', 'past')], max_length=100)),
                ('priority', models.CharField(choices=[('large', 'large'), ('small', 'small')], max_length=50)),
                ('title', models.CharField(max_length=40)),
                ('timing', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('description1', models.CharField(blank=True, max_length=1000)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='news')),
                ('status', models.CharField(choices=[('upcoming', 'upcoming'), ('past', 'past'), ('retired', 'retired')], max_length=10)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('timing', models.CharField(blank=True, max_length=500)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.CharField(max_length=500)),
                ('description3', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='news')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Event')),
            ],
            options={
                'db_table': 'event updates',
            },
        ),
    ]
