# Generated by Django 3.0.6 on 2020-07-01 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]
