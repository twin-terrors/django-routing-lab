from django.contrib import admin

from .models import (
    Genre,
    Composer,
    Hall,
    Collective,
    Artist,
    Work,
    Concert,
    Ticket,
)


admin.site.register(Genre)
admin.site.register(Composer)
admin.site.register(Hall)
admin.site.register(Collective)
admin.site.register(Artist)
admin.site.register(Work)
admin.site.register(Concert)
admin.site.register(Ticket)