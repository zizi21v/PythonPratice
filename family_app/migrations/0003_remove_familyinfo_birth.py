# Generated by Django 4.0.6 on 2022-07-24 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family_app', '0002_alter_familyinfo_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyinfo',
            name='birth',
        ),
    ]
