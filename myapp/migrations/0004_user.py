# Generated by Django 4.0.5 on 2022-06-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
