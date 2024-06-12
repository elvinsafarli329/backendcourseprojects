from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', myBlogViewSet)

urlpatterns = [
    path('list/', RaceAPIpage.as_view(), name="api-list"),
    path('', include(router.urls)),
    path('detail/<pk>', RaceDetailAPIpage.as_view(), name="api-detail"),
    path('delete/<pk>', RaceDeleteAPIpage.as_view(), name="api-delete"),
    path('update/<pk>', RaceUpdateAPIpage.as_view(), name="api-update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


