from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Movies


class MoviesListView(ListView):
    template_name = "Movies/Movies-list.html"
    model = Movies


class MoviesDetailView(DetailView):
    template_name = "Movies/Movies-detail.html"
    model = Movies


class MoviesCreateView(CreateView):
    template_name = "Movies/Movies-create.html"
    model = Movies
    fields = ["movie_name","purchaser","desc","Rank"]


class MoviesUpdateView(UpdateView):
    template_name = "Movies/Movies-update.html"
    model = Movies
    fields = ["movie_name","purchaser","desc","Rank"]


class MoviesDeleteView(DeleteView):
    template_name = "Movies/Movies-delete.html"
    model = Movies
    success_url = reverse_lazy("movie-list")