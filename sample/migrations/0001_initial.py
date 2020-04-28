# Generated by Django 3.0.5 on 2020-04-28 16:22

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=100)),
                ('source_type', models.CharField(blank=True, choices=[(1, 'source-choice-1'), (2, 'source-choice-2'), (3, 'source-choice-3')], max_length=20, null=True)),
                ('source_id', models.CharField(blank=True, max_length=50, null=True)),
                ('input_meta_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
