# Generated by Django 5.0.1 on 2024-02-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0004_adminmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_choose_image', models.ImageField(upload_to='static/uploads/')),
                ('why_choose_title', models.CharField(max_length=200)),
                ('why_choose_details', models.TextField()),
                ('why_choose_since', models.TextField()),
                ('why_choose_selector', models.CharField(max_length=200)),
            ],
        ),
    ]
