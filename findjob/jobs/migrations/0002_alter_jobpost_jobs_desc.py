# Generated by Django 3.2.6 on 2021-09-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='jobs_desc',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
