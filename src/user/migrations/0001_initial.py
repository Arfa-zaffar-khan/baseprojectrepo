# Generated by Django 5.1.1 on 2024-10-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
