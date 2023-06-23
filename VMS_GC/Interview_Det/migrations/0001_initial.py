# Generated by Django 4.2.2 on 2023-06-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('candidate_email', models.EmailField(max_length=254)),
                ('interviewer_email', models.EmailField(max_length=254)),
                ('additional_people_email', models.EmailField(blank=True, max_length=254)),
                ('google_meet_link', models.URLField(blank=True)),
                ('interview_time', models.DateTimeField()),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
    ]
