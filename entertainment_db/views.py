from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Exists
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, DetailView
from pip._vendor import requests

from entertainment_db.forms import AssessmentForm, StatusUserContentForm
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
            Content.objects.create(title=response['Title'], synopsis=response['Plot'],
                                   airdate=datetime.strptime(response['Released'], "%d %b %Y"),
                                   type=response['Type'], id_in_api=id_content, poster_url=response['Poster']).save()
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


@login_required
def search_bar(request):
    if request.method == 'GET':
        search_word = request.GET['q']
        content = list()
        response = requests.get(f'http://www.omdbapi.com/?s={search_word}&apikey=329c0d5e').json()
        for data in response['Search']:
            content.append({"id": data['imdbID'], "name": data['Title'], "type": data['Type'], "img": data['Poster']})
        return JsonResponse({"total_count": len(content), "items": content})


@login_required
def update_status(request, content_id):
    if request.method == 'POST':
        status = request.POST.get("type", "")
        review = request.POST.get("review", "")
        actual_status = StatusUserContent.objects.filter(user=request.user, content__pk=content_id)
        if actual_status:
            if request.user.pk == actual_status[0].user.pk:
                actual_status[0].type = status
                if review:
                    actual_status[0].review = review
                actual_status[0].save()
            else:
                return HttpResponseForbidden()
        else:
            StatusUserContent.objects.create(content_id=content_id, user=request.user, type=status,
                                             review=review).save()
        return redirect(reverse_lazy("content:info", kwargs={'pk': content_id}))


class ContentDetailView(DetailView):
    model = Content
    template_name = 'info.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(self.object.title)
        actual_status = StatusUserContent.objects.filter(user=self.request.user, content__pk=self.object.pk)
        if actual_status:
            context['status_content'] = {'exists': 1, 'value': actual_status[0].type, 'review': actual_status[0].review}
        context['status_form'] = StatusUserContentForm()
        return context
