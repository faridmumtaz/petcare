# Generated by Django 4.0.5 on 2022-07-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_adoption_approve_alter_feedback_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='enable',
            field=models.BooleanField(default=False),
        ),
    ]
