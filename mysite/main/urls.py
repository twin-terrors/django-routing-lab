from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    # Основные страницы
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/location/', views.location, name='location'),

    # Концерты
    path(
        'afisha/',
        views.ConcertListView.as_view(),
        name='concert_list',
    ),
    path(
        'afisha/add/',
        views.ConcertCreateView.as_view(),
        name='concert_create',
    ),
    path(
        'afisha/<int:pk>/',
        views.ConcertDetailView.as_view(),
        name='concert_detail',
    ),
    path(
        'afisha/<int:pk>/edit/',
        views.ConcertUpdateView.as_view(),
        name='concert_update',
    ),
    path(
        'afisha/<int:pk>/delete/',
        views.ConcertDeleteView.as_view(),
        name='concert_delete',
    ),

    # Коллективы
    path(
        'collectives/',
        views.CollectiveListView.as_view(),
        name='collective_list',
    ),
    path(
        'collectives/add/',
        views.CollectiveCreateView.as_view(),
        name='collective_create',
    ),
    path(
        'collectives/<int:pk>/',
        views.CollectiveDetailView.as_view(),
        name='collective_detail',
    ),
    path(
        'collectives/<int:pk>/edit/',
        views.CollectiveUpdateView.as_view(),
        name='collective_update',
    ),
    path(
        'collectives/<int:pk>/delete/',
        views.CollectiveDeleteView.as_view(),
        name='collective_delete',
    ),

    # Артисты
    path(
        'artists/',
        views.ArtistListView.as_view(),
        name='artist_list',
    ),
    path(
        'artists/add/',
        views.ArtistCreateView.as_view(),
        name='artist_create',
    ),
    path(
        'artists/<int:pk>/',
        views.ArtistDetailView.as_view(),
        name='artist_detail',
    ),
    path(
        'artists/<int:pk>/edit/',
        views.ArtistUpdateView.as_view(),
        name='artist_update',
    ),
    path(
        'artists/<int:pk>/delete/',
        views.ArtistDeleteView.as_view(),
        name='artist_delete',
    ),

    # Залы
    path(
        'halls/',
        views.HallListView.as_view(),
        name='hall_list',
    ),
    path(
        'halls/add/',
        views.HallCreateView.as_view(),
        name='hall_create',
    ),
    path(
        'halls/<int:pk>/',
        views.HallDetailView.as_view(),
        name='hall_detail',
    ),
    path(
        'halls/<int:pk>/edit/',
        views.HallUpdateView.as_view(),
        name='hall_update',
    ),
    path(
        'halls/<int:pk>/delete/',
        views.HallDeleteView.as_view(),
        name='hall_delete',
    ),

    # Произведения
    path(
        'works/',
        views.WorkListView.as_view(),
        name='work_list',
    ),
    path(
        'works/add/',
        views.WorkCreateView.as_view(),
        name='work_create',
    ),
    path(
        'works/<int:pk>/',
        views.WorkDetailView.as_view(),
        name='work_detail',
    ),
    path(
        'works/<int:pk>/edit/',
        views.WorkUpdateView.as_view(),
        name='work_update',
    ),
    path(
        'works/<int:pk>/delete/',
        views.WorkDeleteView.as_view(),
        name='work_delete',
    ),
]