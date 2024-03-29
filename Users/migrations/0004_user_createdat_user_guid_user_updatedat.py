# Generated by Django 5.0.2 on 2024-02-20 16:02

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_user_auttype_alter_user_sex_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
