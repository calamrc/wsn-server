# Generated by Django 3.1.1 on 2020-09-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_wsn_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='wsn',
            name='timestamp',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]