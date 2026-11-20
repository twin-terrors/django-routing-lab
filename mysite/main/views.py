from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import (
    ConcertForm,
    CollectiveForm,
    ArtistForm,
    HallForm,
    WorkForm,
)
from .models import Concert, Collective, Artist, Hall, Work


# Страницы первой практической работы

def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def location(request):
    return render(request, 'main/location.html')


def afisha(request):
    return render(request, 'main/afisha.html')


def collectives(request):
    return render(request, 'main/collectives.html')


# Обработка удаления записей, на которые есть ссылки

class ProtectedDeleteView(DeleteView):
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            context = self.get_context_data(form=form)
            context['delete_error'] = (
                'Нельзя удалить запись: с ней связаны другие данные. '
                'Сначала удалите связанные записи или измените их связи.'
            )
            return self.render_to_response(context)


# Концерты

class ConcertListView(ListView):
    model = Concert
    template_name = 'main/concerts/list.html'
    context_object_name = 'concerts'
    ordering = ['date', 'pk']


class ConcertDetailView(DetailView):
    model = Concert
    template_name = 'main/concerts/detail.html'
    context_object_name = 'concert'


class ConcertCreateView(CreateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'main/concerts/form.html'
    success_url = reverse_lazy('main:concert_list')


class ConcertUpdateView(UpdateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'main/concerts/form.html'
    success_url = reverse_lazy('main:concert_list')


class ConcertDeleteView(ProtectedDeleteView):
    model = Concert
    template_name = 'main/concerts/confirm_delete.html'
    success_url = reverse_lazy('main:concert_list')


# Коллективы

class CollectiveListView(ListView):
    model = Collective
    template_name = 'main/collectives/list.html'
    context_object_name = 'collectives'
    ordering = ['name', 'pk']


class CollectiveDetailView(DetailView):
    model = Collective
    template_name = 'main/collectives/detail.html'
    context_object_name = 'collective'


class CollectiveCreateView(CreateView):
    model = Collective
    form_class = CollectiveForm
    template_name = 'main/collectives/form.html'
    success_url = reverse_lazy('main:collective_list')


class CollectiveUpdateView(UpdateView):
    model = Collective
    form_class = CollectiveForm
    template_name = 'main/collectives/form.html'
    success_url = reverse_lazy('main:collective_list')


class CollectiveDeleteView(ProtectedDeleteView):
    model = Collective
    template_name = 'main/collectives/confirm_delete.html'
    success_url = reverse_lazy('main:collective_list')


# Артисты

class ArtistListView(ListView):
    model = Artist
    template_name = 'main/artists/list.html'
    context_object_name = 'artists'
    ordering = ['name', 'pk']


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'main/artists/detail.html'
    context_object_name = 'artist'


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'main/artists/form.html'
    success_url = reverse_lazy('main:artist_list')


class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'main/artists/form.html'
    success_url = reverse_lazy('main:artist_list')


class ArtistDeleteView(ProtectedDeleteView):
    model = Artist
    template_name = 'main/artists/confirm_delete.html'
    success_url = reverse_lazy('main:artist_list')


# Залы

class HallListView(ListView):
    model = Hall
    template_name = 'main/halls/list.html'
    context_object_name = 'halls'
    ordering = ['name', 'pk']


class HallDetailView(DetailView):
    model = Hall
    template_name = 'main/halls/detail.html'
    context_object_name = 'hall'


class HallCreateView(CreateView):
    model = Hall
    form_class = HallForm
    template_name = 'main/halls/form.html'
    success_url = reverse_lazy('main:hall_list')


class HallUpdateView(UpdateView):
    model = Hall
    form_class = HallForm
    template_name = 'main/halls/form.html'
    success_url = reverse_lazy('main:hall_list')


class HallDeleteView(ProtectedDeleteView):
    model = Hall
    template_name = 'main/halls/confirm_delete.html'
    success_url = reverse_lazy('main:hall_list')


# Произведения

class WorkListView(ListView):
    model = Work
    template_name = 'main/works/list.html'
    context_object_name = 'works'
    ordering = ['name', 'pk']


class WorkDetailView(DetailView):
    model = Work
    template_name = 'main/works/detail.html'
    context_object_name = 'work'


class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'main/works/form.html'
    success_url = reverse_lazy('main:work_list')


class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'main/works/form.html'
    success_url = reverse_lazy('main:work_list')


class WorkDeleteView(ProtectedDeleteView):
    model = Work
    template_name = 'main/works/confirm_delete.html'
    success_url = reverse_lazy('main:work_list')