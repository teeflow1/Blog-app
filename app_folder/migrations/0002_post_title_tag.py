# Generated by Django 4.2.2 on 2023-06-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='This is a blog web app!!!!', max_length=250),
        ),
    ]
