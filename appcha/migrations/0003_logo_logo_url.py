# Generated by Django 4.1.3 on 2023-03-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcha', '0002_alter_logo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='logo_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
