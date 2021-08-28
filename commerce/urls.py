from django.urls import path

from .views import SearchResultsView, HomePageView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_page'),
    path('', HomePageView.as_view(), name='home'),
]
