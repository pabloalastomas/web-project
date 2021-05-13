"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from entertainment_db.views import *

app_name = 'content'

urlpatterns = [
    path('search/', search_bar, name='content_search'),
    path('search/go/', search_bar_redirect, name='content_search_go'),
    path('rating/', rating, name='rating'),
    path('info/<int:pk>/', ContentDetailView.as_view(), name='info'),
    path('update-status/<int:content_id>/', update_status, name='update-status'),
    path('platform/add/<int:id>/', PlatformContentCreateView.as_view(), name='add_in_platform'),
    path('platform/delete/<int:pk>/', PlatformContentDeleteView.as_view(), name='delete_in_platform'),

]
