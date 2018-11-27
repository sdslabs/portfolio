# Generated by Django 2.1.3 on 2018-11-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permalink', models.CharField(max_length=40, unique=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='projects')),
                ('is_visible', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
