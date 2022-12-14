# Generated by Django 3.2.6 on 2022-09-04 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('right_answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.theme')),
                ('wrong_answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='default', to='questions.answer')),
            ],
        ),
    ]
