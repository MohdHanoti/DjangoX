from django.urls import path
from .views import MoviesListView, MoviesDetailView, MoviesCreateView, MoviesUpdateView, MoviesDeleteView

urlpatterns = [
    path('movie/', MoviesListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MoviesDetailView.as_view(), name='movie-detail'),
    path('movie/create/', MoviesCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/update/', MoviesUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', MoviesDeleteView.as_view(), name='movie-delete'),
]
