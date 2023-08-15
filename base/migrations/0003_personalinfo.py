# Generated by Django 4.2.4 on 2023-08-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_sitesettings_sitesetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_pic', models.ImageField(upload_to='profile_pics/')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('bio', models.TextField()),
            ],
        ),
    ]