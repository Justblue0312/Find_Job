# Generated by Django 3.2.6 on 2021-09-29 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210923_0112'),
        ('jobs', '0006_application_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_checked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.lecture'),
        ),
    ]
