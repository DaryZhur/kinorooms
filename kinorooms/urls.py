from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from kino.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
