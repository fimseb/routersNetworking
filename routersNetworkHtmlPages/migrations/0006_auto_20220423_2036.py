# Generated by Django 3.0 on 2022-04-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routersNetworkHtmlPages', '0005_dot_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dot',
            name='pdf',
            field=models.FileField(upload_to='dots'),
        ),
    ]
