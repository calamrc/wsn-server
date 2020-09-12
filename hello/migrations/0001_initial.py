# Generated by Django 3.1.1 on 2020-09-12 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='captcha/')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WSN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wsn_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WSNDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.sensor')),
                ('wsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.wsn')),
            ],
        ),
        migrations.AddField(
            model_name='wsn',
            name='sensors',
            field=models.ManyToManyField(through='hello.WSNDetails', to='hello.Sensor'),
        ),
    ]
