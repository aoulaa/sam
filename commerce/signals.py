from django.contrib.postgres.search import SearchVector
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product


@receiver(post_save, sender=Product)
def update_search_vector(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search=(
        SearchVector('title', weight='A')
    ))
