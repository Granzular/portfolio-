# Generated by Django 5.1.5 on 2025-03-21 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_quiz_options_remove_quiz_users_who_attempted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='value',
        ),
    ]
