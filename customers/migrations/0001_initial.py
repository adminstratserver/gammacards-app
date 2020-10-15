# Generated by Django 3.0.7 on 2020-07-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('agent', models.CharField(default='NIL', max_length=100)),
                ('profile_pic', models.ImageField(blank=True, default='photos/pic1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
