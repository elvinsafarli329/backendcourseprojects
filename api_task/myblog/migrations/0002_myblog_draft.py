# Generated by Django 5.0.6 on 2024-06-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
