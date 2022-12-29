# Generated by Django 4.0.6 on 2022-08-23 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('Donerid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=45)),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.TextField(verbose_name=45)),
                ('Email', models.EmailField(max_length=45)),
                ('Gender', models.CharField(max_length=6)),
                ('Phone', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('CityName', models.CharField(max_length=45)),
                ('Bloodgroup', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=45)),
                ('Phone', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doner_id', models.CharField(max_length=20)),
                ('Subject', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=200)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=45)),
                ('Feedbacktext', models.TextField()),
                ('Rating', models.IntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Health_Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campaign_Name', models.CharField(max_length=100)),
                ('Organizer_Name', models.CharField(max_length=45)),
                ('Venue', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
