# Generated by Django 5.1 on 2024-08-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mplace', models.CharField(max_length=25)),
                ('mdate', models.DateField()),
                ('cpn1', models.CharField(max_length=25)),
                ('cpnum1', models.IntegerField()),
                ('cpn2', models.CharField(max_length=25)),
                ('cpnn2', models.IntegerField()),
                ('fn', models.CharField(max_length=25)),
                ('mn', models.CharField(max_length=25)),
                ('gn', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('passwd', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
