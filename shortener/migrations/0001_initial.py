# Generated by Django 3.0.7 on 2020-06-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('origin_url', models.URLField(max_length=500, unique=True)),
                ('short_path', models.URLField(max_length=5, unique=True)),
            ],
        ),
    ]