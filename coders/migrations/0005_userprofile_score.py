# Generated by Django 2.1.7 on 2019-04-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coders', '0004_auto_20190326_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
