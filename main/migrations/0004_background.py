# Generated by Django 3.2 on 2021-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('start', models.CharField(max_length=30)),
                ('end', models.CharField(max_length=30)),
            ],
        ),
    ]
