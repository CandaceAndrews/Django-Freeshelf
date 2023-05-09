"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from resources import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.list_resources, name="home"),
    path('resource/new', views.add_resource, name="add_resource"),
    path("resources/<int:pk>", views.details_about_resource,
         name="details_about_resource"),
    path('accounts/', include('registration.backends.simple.urls')),
    # access to django registration redux
    path('category/<slug:slug>', views.resource_category, name="category"),
    path('book/favorite/<int:pk>', views.favorite_book, name='favorite'),
]
