# Generated by Django 4.2.2 on 2023-07-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
