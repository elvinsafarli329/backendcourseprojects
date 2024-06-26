"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from movies.views import *
from movies.views import ChangePasswordView

urlpatterns = [
    path("", main_page, name = "main" ),
    path("about/", about_page, name="about"),
    path("movies/", movies_page, name="movies"),
    path("add/", add_movies_page, name="add-movies"),
    path("settings/", ChangePasswordView.as_view(), name="settings"),
    path("update/<int:id>", update_movies_page, name="update"),
    path("delete-movies/<int:id>", delete_movies_page, name="delete"),
    path("account/", include("account.urls")),
    path('detail/<int:id>', detail_page, name = "detail"),
    path("addcomment/<int:id>", add_comment, name="comment" ),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)