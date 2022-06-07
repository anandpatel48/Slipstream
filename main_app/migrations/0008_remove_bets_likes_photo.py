# Generated by Django 4.0.5 on 2022-06-07 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_bets_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bets',
            name='likes',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bets')),
            ],
        ),
    ]
