from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView
from pip._vendor import requests

from entertainment_db.forms import *
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_status'] = StatusUserContent.objects.filter(user=self.request.user)
        context['user_ratings'] = Assessment.objects.filter(user=self.request.user)
        return context


@login_required
def rating(request):
    if request.method == 'GET':
        id_content = request.GET['content']
        rating = request.GET['rating']
        record = Assessment.objects.filter(content__pk=id_content, user=request.user)
        if not record:
            Assessment.objects.create(content_id=id_content, user=request.user, rating=rating)
        else:
            record[0].rating = rating
            record[0].save()
        return HttpResponse()


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
def search_bar_redirect(request):
    if request.method == 'POST':
        id_content = request.POST.get("search_bar", "")
        content = Content.objects.filter(id_in_api=id_content)
        if not content:
            response = requests.get(f'http://www.omdbapi.com/?i={id_content}&apikey=329c0d5e').json()
            if response['Poster'] == "N/A":
                poster = "https://gaprastore.com/wp-content/uploads/2020/12/no_image-1.jpg"
            else:
                poster = response['Poster']
            content = Content.objects.create(title=response['Title'], synopsis=response['Plot'],
                                             airdate=datetime.strptime(response['Released'], "%d %b %Y"),
                                             type=response['Type'], id_in_api=id_content, poster_url=poster)
            content.save()
        else:
            content = content[0]
        return redirect(reverse_lazy("content:info", kwargs={'pk': content.pk}))


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
        actual_status = StatusUserContent.objects.filter(user=self.request.user, content__pk=self.object.pk)
        if actual_status:
            context['status_content'] = {'exists': 1, 'value': str(actual_status[0].type), 'review': actual_status[0].review}
        actual_rating = Assessment.objects.filter(user=self.request.user, content__pk=self.object.pk)
        if actual_rating:
            context['status_rating'] = {'exists': True, 'value': str(actual_rating[0].rating)}
        context['status_form'] = StatusUserContentForm()
        context['global_rating'] = Assessment.objects.all().aggregate(Avg('rating'))
        context['links'] = PlatformContent.objects.filter(content__pk=self.object.pk)
        return context


class PlatformContentCreateView(CreateView):
    model = PlatformContent
    form_class = PlatformContentForm
    template_name = 'form.html'
    success_url = reverse_lazy('profile')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        if self.kwargs['id']:
            content = Content.objects.get(id=self.kwargs['id'])
            form.fields['content'].initial = content
            form.fields['user'].initial = self.request.user
            form.fields['user'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Título de la Página
        context['title'] = 'Add link to a streaming platform'
        return context


class PlatformContentDeleteView(DeleteView):
    model = PlatformContent
    form_class = PlatformContentForm
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        content = PlatformContent.objects.get(pk=self.kwargs['pk'])
        if content.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Título de la Página
        context['title'] = 'Delete link from a streaming platform'
        return context
