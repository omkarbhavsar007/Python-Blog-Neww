# Generated by Django 5.0.1 on 2024-01-31 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(upload_to='static/uploads/')),
                ('slider_title', models.CharField(max_length=200)),
                ('slider_heading', models.CharField(max_length=200)),
                ('slider_button_heading', models.CharField(max_length=200)),
                ('slider_button_link', models.CharField(max_length=200)),
            ],
        ),
    ]
