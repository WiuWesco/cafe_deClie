# Generated by Django 4.0.1 on 2022-04-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0015_alter_feedback_options_alter_galary_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
