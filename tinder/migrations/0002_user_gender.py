# Generated by Django 4.0.3 on 2023-01-17 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default=django.utils.timezone.now, max_length=100, verbose_name='Gender'),
            preserve_default=False,
        ),
    ]
