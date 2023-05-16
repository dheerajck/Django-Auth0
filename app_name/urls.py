from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("logout", views.logout_view),
    path("", include("social_django.urls", namespace='social')),
    # path("", include("django.contrib.auth.urls")),
    path('profile/', views.profile, name='profile'),
]
