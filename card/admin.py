from django.contrib import admin
from django.db import models
from django.db.models import Q
from card.models import Teams, Cards, Posts, Persons, PersonOnTeam


admin.site.register(Teams)
admin.site.register(Cards)
admin.site.register(Posts),
admin.site.register(Persons)
admin.site.register(PersonOnTeam)
