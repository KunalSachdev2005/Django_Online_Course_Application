# Generated by Django 4.2.3 on 2024-12-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=50),
        ),
    ]