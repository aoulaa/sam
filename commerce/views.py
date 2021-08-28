

from commerce.models import Product
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import IntegerField, Q
from django.db.models.expressions import Case, F, Value, When
from rest_framework.generics import ListAPIView
from django.contrib.postgres.search import TrigramSimilarity

from django.db.models import Q
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    template_name = 'index.html'
    paginate_by = 2
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('search')
        product_list = Product.objects.annotate(
            exact_rank=Case(
                When(title__iexact=query, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
                    ),
            full_text_rank=SearchRank(F('search'), SearchQuery(query)),
            fuzzy_rank=TrigramSimilarity('title', query)
        ).filter(
            Q(exact_rank=1) |
            Q(full_text_rank__gte=0.3) |
            Q(fuzzy_rank__gte=0.1)
        ).order_by(
            '-exact_rank',
            '-full_text_rank',
            '-fuzzy_rank',
        )
        return product_list
