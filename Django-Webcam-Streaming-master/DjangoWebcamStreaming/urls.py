"""DjangoWebcamStreaming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import StreamingHttpResponse
from django.urls import path
from app import views
from camera import VideoCamera, gen
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.login),
    path('logout/', views.logout_page),
    path('home/', TemplateView.as_view(template_name="home.html")),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),
    path('admin/', admin.site.urls),
]
