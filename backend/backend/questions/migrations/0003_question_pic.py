# Generated by Django 3.2.6 on 2022-09-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pic',
            field=models.ImageField(default=None, upload_to='questions_pic'),
        ),
    ]
