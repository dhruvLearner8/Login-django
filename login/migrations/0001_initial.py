# Generated by Django 3.2 on 2022-12-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=50, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('age', models.IntegerField(default=0)),
                ('full_name', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
    ]