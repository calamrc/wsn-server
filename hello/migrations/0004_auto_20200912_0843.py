# Generated by Django 3.1.1 on 2020-09-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200912_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wsndetails',
            name='when',
            field=models.DateTimeField(auto_now=True),
        ),
    ]