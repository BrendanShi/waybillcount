from django.urls import path, include
from . import views as user_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('account/', user_views.dashboard, name='dashboard'),
]
