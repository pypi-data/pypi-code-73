# Generated by Django 2.2.17 on 2020-12-15 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20200902_1545'),
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='featured_image',
            field=models.ForeignKey(default=None, help_text='Only jpg, gif, or png images.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapters', to='files.File'),
        ),
    ]
