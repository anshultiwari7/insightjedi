from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from sample import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'documents', views.DocumentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]