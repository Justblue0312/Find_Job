# Generated by Django 3.2.6 on 2021-09-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_application_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
