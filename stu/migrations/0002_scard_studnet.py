# Generated by Django 3.0.8 on 2020-07-15 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studnet',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Scard',
            fields=[
                ('st', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stu.Studnet')),
                ('major', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'scard',
            },
        ),
    ]
