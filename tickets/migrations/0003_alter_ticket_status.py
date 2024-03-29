# Generated by Django 4.1.5 on 2023-04-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('FR', 'Frozen'), ('RE', 'Resolved')], default='Pending', max_length=8),
        ),
    ]
