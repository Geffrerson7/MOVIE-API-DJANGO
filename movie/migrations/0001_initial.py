# Generated by Django 4.1.7 on 2023-03-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('genre', models.CharField(max_length=50)),
                ('image', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
