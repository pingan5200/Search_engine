# Generated by Django 2.1.4 on 2019-02-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('weight', models.CharField(max_length=20, verbose_name='重量')),
                ('descibe', models.CharField(max_length=500, verbose_name='描述')),
            ],
        ),
    ]
