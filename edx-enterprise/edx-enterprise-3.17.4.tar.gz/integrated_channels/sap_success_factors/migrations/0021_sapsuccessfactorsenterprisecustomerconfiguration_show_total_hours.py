# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-21 13:41


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap_success_factors', '0020_sapsuccessfactorsenterprisecustomerconfiguration_catalogs_to_transmit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='show_total_hours',
            field=models.BooleanField(default=False, verbose_name='Show Total Hours'),
        ),
    ]
