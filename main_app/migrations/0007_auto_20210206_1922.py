# Generated by Django 3.1.6 on 2021-02-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210206_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='quote',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='writer',
            name='works',
            field=models.TextField(),
        ),
    ]
