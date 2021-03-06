from django.conf import settings
from django.contrib.postgres import fields as psql_fields
from django.db import migrations, models
import django.db.models.deletion

import galaxy.main.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20181018_1248'),
        ('main', '0120_repository_quality_score_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    primary_key=True,
                    serialize=False,
                    to=settings.AUTH_USER_MODEL
                )),
                ('preferences', psql_fields.JSONField(default=dict)),
                ('namespaces_followed', models.ManyToManyField(
                    blank=True,
                    to='main.Namespace'
                )),
                ('repositories_followed', models.ManyToManyField(
                    blank=True,
                    to='main.Repository'
                )),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, galaxy.main.mixins.DirtyMixin),
        ),
    ]
