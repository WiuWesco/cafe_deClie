# Generated by Django 4.0.1 on 2022-02-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0008_alter_store_chapter_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_chapter',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
