# Generated by Django 5.0.3 on 2024-03-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_alter_books_options_alter_college_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="student_id",
            field=models.CharField(default=0, max_length=100, verbose_name="学号"),
            preserve_default=False,
        ),
    ]
