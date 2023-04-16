# Generated by Django 4.1.5 on 2023-03-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectionCode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('voted', models.BooleanField(default=False)),
                ('student_id', models.CharField(max_length=200)),
            ],
        ),
    ]
