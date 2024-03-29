# Generated by Django 3.0 on 2022-03-24 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routersNetworkHtmlPages', '0003_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_assign_by_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_assign', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_assign_to_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_given', to=settings.AUTH_USER_MODEL),
        ),
    ]
