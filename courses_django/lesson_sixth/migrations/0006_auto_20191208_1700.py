# Generated by Django 2.2.7 on 2019-12-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_sixth', '0005_auto_20191208_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='sex',
            field=models.BooleanField(default=True),
        ),
    ]
