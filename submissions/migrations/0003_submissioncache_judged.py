# Generated by Django 2.1.7 on 2019-04-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_remove_mainsubmission_sidno'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissioncache',
            name='judged',
            field=models.CharField(blank=True, default='no', max_length=5),
        ),
    ]
