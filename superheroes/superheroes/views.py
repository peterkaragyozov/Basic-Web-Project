from django import forms
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from superheroes.models import Superhero


class SuperheroesListView(ListView):
    model = Superhero
    template_name = "superheroes.html"
    queryset = Superhero.objects.all()
    context_object_name = "superhero_list"

class SuperheroForm(forms.Form):
    name = forms.CharField(label="Name")
    secret_identity = forms.CharField(label="Secret Identity")

    def save(self):
        name = self.cleaned_data['name']
        secret_identity = self.cleaned_data['secret_identity']
        superhero = Superhero(name=name, secret_identity=secret_identity)
        superhero.save()


class SuperheroCreateView(View):
    template_name = "superhero-create.html"
    def get(self, request):
        form = SuperheroForm()
        return render(request, self.template_name, { 'form': form })

    def post(self, request):
        form = SuperheroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
