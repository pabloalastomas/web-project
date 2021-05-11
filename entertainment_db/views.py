from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Exists
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from pip._vendor import requests

from entertainment_db.forms import AssessmentForm
from entertainment_db.models import *
from datetime import datetime


# Create your views here.


class UserRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class UserProfileView(TemplateView):
    template_name = 'profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AssessmentCreateView(CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = 'rating.html'
    success_url = reverse_lazy('profile')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        return form

    def post(self, request, *args, **kwargs):
        rating = request.POST.get("rating", "")
        id_content = request.POST.get("search_bar", "")
        if not Content.objects.filter(id_in_api=id_content):
            response = requests.get(f'http://www.omdbapi.com/?i={id_content}&apikey=329c0d5e').json()
            Content.objects.create(title=response['Title'], synopsis=response['Plot'], airdate=datetime.strptime(response['Released'], "%d %b %Y"),
                                   type=response['Type'], id_in_api=id_content).save()
        try:
            record = Assessment.objects.filter(content=Content.objects.get(id_in_api=id_content), user=request.user)
            if not record:
                Assessment.objects.create(content=Content.objects.get(id_in_api=id_content), user=request.user,
                                      rating=rating)
            else:
                record[0].rating = rating
                record[0].save()
            return redirect("profile")
        except:
            return render(request, 'rating.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Título de la Página
        context['title'] = 'Añadir Actividad'
        # Path de donde nos encontramos dentro de la página
        context['menu'] = [
            {'url': reverse_lazy('erp:activities_list'), 'name': 'Actividades'},
            {'url': reverse_lazy('erp:activities_create'), 'name': 'Nueva Actividad'}
        ]
        # Nombre del Botón
        context['name'] = 'Crear Actividad'
        context['content'] = '¿Estás seguro de que quieres añadir la actividad?'
        return context
