from django.contrib import admin
from django.urls import path

from superheroes.views import SuperheroesListView, SuperheroCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SuperheroesListView.as_view()),
    path('superhero-create/', SuperheroCreateView.as_view(), name="create superhero"),
]
