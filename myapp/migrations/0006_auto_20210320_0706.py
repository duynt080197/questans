# Generated by Django 2.2.19 on 2021-03-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='down',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='up',
            field=models.IntegerField(default=0),
        ),
    ]
