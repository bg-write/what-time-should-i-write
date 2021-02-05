# Generated by Django 3.1.6 on 2021-02-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('dawn', models.TextField(max_length=1000)),
                ('sunrise', models.TextField(max_length=1000)),
                ('morning', models.TextField(max_length=1000)),
                ('noon', models.TextField(max_length=1000)),
                ('afternoon', models.TextField(max_length=1000)),
                ('evening', models.TextField(max_length=1000)),
                ('sunset', models.TextField(max_length=1000)),
                ('dusk', models.TextField(max_length=1000)),
                ('night', models.TextField(max_length=1000)),
                ('midnight', models.TextField(max_length=1000)),
                ('source', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth', models.IntegerField()),
                ('death', models.IntegerField()),
                ('works', models.TextField(max_length=500)),
                ('quote', models.TextField(max_length=1000)),
            ],
        ),
    ]
