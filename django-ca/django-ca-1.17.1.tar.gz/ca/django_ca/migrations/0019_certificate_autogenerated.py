# Generated by Django 3.0.2 on 2020-01-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0018_certificate_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='autogenerated',
            field=models.BooleanField(default=False, help_text='If this certificate was automatically generated.'),
        ),
    ]
