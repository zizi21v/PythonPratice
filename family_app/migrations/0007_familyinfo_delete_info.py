# Generated by Django 4.0.6 on 2022-07-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_app', '0006_remove_info_cumpleaños'),
    ]

    operations = [
        migrations.CreateModel(
            name='familyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('cumpleaños', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='info',
        ),
    ]
