# Generated by Django 3.2.12 on 2023-04-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='link',
            field=models.CharField(max_length=400),
        ),
    ]