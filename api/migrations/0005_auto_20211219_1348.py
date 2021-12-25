# Generated by Django 3.1.2 on 2021-12-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211219_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizarchive',
            name='option_five',
        ),
        migrations.AddField(
            model_name='quizarchive',
            name='correct_anwser',
            field=models.CharField(choices=[('option_one', 'Option One'), ('option_two', 'Option Two'), ('option_three', 'Option Three'), ('option_four', 'Option Four')], default=True, max_length=150),
            preserve_default=False,
        ),
    ]