from django.contrib.postgres.operations import TrigramExtension, CreateCollation
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import migrations


def update_search_vector(apps, schema_editor):
    Product = apps.get_model('commerce', 'Product')
    Product.objects.all().update(search=(
        SearchVector('title', weight='A')
    ))


class Migration(migrations.Migration):
    dependencies = [
        ('commerce', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='Product',
            name='search',
            field=SearchVectorField(blank=True, null=True),
        ),
        migrations.RunPython(update_search_vector),
    ]
