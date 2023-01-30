# Generated by Django 4.1.3 on 2023-01-30 08:49

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='uploads')),
                ('token', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='userLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(blank=True, max_length=200, null=True)),
                ('batch', models.CharField(blank=True, max_length=500, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('credithour', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('gradevalu', models.CharField(blank=True, max_length=300, null=True)),
                ('lcgpa', models.CharField(blank=True, max_length=200, null=True)),
                ('semlettergrade', models.CharField(blank=True, max_length=400, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('symb', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
