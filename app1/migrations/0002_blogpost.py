# Generated by Django 3.1.3 on 2020-11-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('catagory', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('textarea', models.TextField()),
                ('email', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
