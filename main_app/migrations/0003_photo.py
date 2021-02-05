# Generated by Django 3.1.6 on 2021-02-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_routine_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.writer')),
            ],
        ),
    ]