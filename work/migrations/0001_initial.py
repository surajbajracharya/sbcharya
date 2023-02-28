# Generated by Django 4.1.7 on 2023-02-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='work/images/')),
                ('content', models.TextField()),
                ('reference', models.CharField(max_length=255)),
            ],
        ),
    ]