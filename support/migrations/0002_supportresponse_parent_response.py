# Generated by Django 4.1.5 on 2023-02-22 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportresponse',
            name='parent_response',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='responses', to='support.supportresponse'),
        ),
    ]
