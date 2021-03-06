# Generated by Django 3.2.3 on 2021-05-28 20:26

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50)),
                ('project_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=' screenshot')),
                ('project_description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('voters', models.IntegerField(default=0)),
                ('link', models.URLField()),
                ('author', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
