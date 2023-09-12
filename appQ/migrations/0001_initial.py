# Generated by Django 4.2.1 on 2023-09-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('exp_level', models.FloatField(default=0)),
                ('aim', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.CharField(default='Q0000', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('toughness', models.FloatField(default=0)),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('dateOfTest', models.DateField(auto_now_add=True)),
                ('percentage', models.FloatField(default=0)),
                ('exp_at_test', models.IntegerField(default=0)),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
    ]
