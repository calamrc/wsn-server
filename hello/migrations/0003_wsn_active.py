# Generated by Django 3.1.1 on 2020-09-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_wsn_battery'),
    ]

    operations = [
        migrations.AddField(
            model_name='wsn',
            name='active',
            field=models.CharField(default='yes', max_length=10),
            preserve_default=False,
        ),
    ]