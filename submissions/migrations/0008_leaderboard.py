# Generated by Django 2.1.7 on 2019-04-05 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0007_auto_20190405_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('user_handle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_leaderboard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
