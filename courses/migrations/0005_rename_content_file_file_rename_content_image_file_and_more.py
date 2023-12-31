# Generated by Django 4.1.11 on 2023-09-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='content',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='content',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='content',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='content',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
