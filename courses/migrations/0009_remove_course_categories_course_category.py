# Generated by Django 4.1.3 on 2024-07-08 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_course_category_course_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='categories',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
    ]
