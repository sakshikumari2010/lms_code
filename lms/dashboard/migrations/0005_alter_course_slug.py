# Generated by Django 4.0.4 on 2022-05-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_course_slug_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
