from django import forms

from .models import Concert, Collective, Artist, Hall, Work


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = [
            'name',
            'description',
            'date',
            'price',
            'hall',
            'genre',
            'collective',
            'poster',
        ]
        widgets = {
            'date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'},
            ),
        }


class CollectiveForm(forms.ModelForm):
    class Meta:
        model = Collective
        fields = [
            'name',
            'description',
            'photo',
        ]


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
            'biography',
            'collective',
            'photo',
        ]


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = [
            'name',
            'description',
            'capacity',
        ]


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = [
            'name',
            'composer',
            'duration',
            'description',
        ]