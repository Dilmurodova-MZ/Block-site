# Generated by Django 4.1.7 on 2023-03-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcha', '0009_alter_blog_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField()),
            ],
            options={
                'verbose_name': 'Gallereya',
                'verbose_name_plural': 'Gallereyalar',
            },
        ),
    ]