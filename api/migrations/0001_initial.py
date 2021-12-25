# Generated by Django 3.1.2 on 2021-12-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizeArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=350)),
                ('option_two', models.CharField(blank=True, max_length=350)),
                ('option_three', models.CharField(blank=True, max_length=350)),
                ('option_four', models.CharField(blank=True, max_length=350)),
                ('option_five', models.CharField(blank=True, max_length=350)),
                ('correct_anwser', models.CharField(blank=True, max_length=350)),
            ],
            options={
                'verbose_name_plural': 'Quiz Archive',
            },
        ),
    ]