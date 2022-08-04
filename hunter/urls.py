"""hunter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, topic_details, home, HunterProfile, register, FeedbackCreateView, feedback_details
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('index/', index, name="index"),
    path('topic/<int:pk>/', topic_details, name="topic_details"),
    path('profile/', HunterProfile.as_view(), name="profile"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', register, name="register"),
    path('add_place/', FeedbackCreateView.as_view(), name="feedback-creat"),
    path('feedback/<int:pk>', feedback_details, name="feedback_details"),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
