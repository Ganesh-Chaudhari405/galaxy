import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0129_collection_quality_score_updates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='quality_score',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='quality_score_date',
        ),
        migrations.AddField(
            model_name='collectionversion',
            name='quality_score',
            field=models.FloatField(
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
