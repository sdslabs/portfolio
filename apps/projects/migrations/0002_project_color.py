# Generated by Django 2.2.4 on 2020-01-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]