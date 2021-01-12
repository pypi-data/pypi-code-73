# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-24 15:08


import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0015_auto_20170130_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogTransmissionAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('enterprise_customer_uuid', models.UUIDField()),
                ('total_courses', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=100)),
                ('error_message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSAPSuccessFactorsEnterpriseCustomerConfiguration',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField()),
                ('sapsf_base_url', models.CharField(max_length=255)),
                ('key', models.CharField(blank=True, max_length=255, verbose_name='Client ID')),
                ('secret', models.CharField(blank=True, max_length=255, verbose_name='Client Secret')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('enterprise_customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.EnterpriseCustomer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical sap success factors enterprise customer configuration',
            },
        ),
        migrations.CreateModel(
            name='LearnerDataTransmissionAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_course_enrollment_id', models.PositiveIntegerField()),
                ('sapsf_user_id', models.CharField(max_length=255)),
                ('course_id', models.CharField(max_length=255)),
                ('course_completed', models.BooleanField(default=True)),
                ('completed_timestamp', models.BigIntegerField()),
                ('instructor_name', models.CharField(blank=True, max_length=255)),
                ('grade', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('error_message', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SAPSuccessFactorsEnterpriseCustomerConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField()),
                ('sapsf_base_url', models.CharField(max_length=255)),
                ('key', models.CharField(blank=True, max_length=255, verbose_name='Client ID')),
                ('secret', models.CharField(blank=True, max_length=255, verbose_name='Client Secret')),
                ('enterprise_customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='SAPSuccessFactorsGlobalConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('completion_status_api_path', models.CharField(max_length=255)),
                ('course_api_path', models.CharField(max_length=255)),
                ('oauth_api_path', models.CharField(max_length=255)),
                ('provider_id', models.CharField(default='EDX', max_length=100)),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
        ),
    ]
