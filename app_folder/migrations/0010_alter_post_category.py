# Generated by Django 4.2.2 on 2023-06-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0009_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
