# Generated by Django 4.2.4 on 2023-08-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_details', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]