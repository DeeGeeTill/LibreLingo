# Generated by Django 3.0.5 on 2020-04-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0032_auto_20200412_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaryitem',
            name='definition',
            field=models.TextField(blank=True),
        ),
    ]