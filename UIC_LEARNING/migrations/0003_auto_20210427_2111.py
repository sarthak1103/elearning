# Generated by Django 3.1.7 on 2021-04-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UIC_LEARNING', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledstudents',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
