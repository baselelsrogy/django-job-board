# Generated by Django 5.1.7 on 2025-04-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
