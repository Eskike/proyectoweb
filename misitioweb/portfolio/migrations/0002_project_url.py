# Generated by Django 4.0.3 on 2023-02-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
