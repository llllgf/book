# Generated by Django 5.0.3 on 2024-03-18 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_student_student_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="books",
            old_name="IECN",
            new_name="ISBN",
        ),
    ]
