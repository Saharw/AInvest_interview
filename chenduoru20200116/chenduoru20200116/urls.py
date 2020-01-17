"""chenduoru20200116 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from user_data import views as user_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.Login.as_view()),
    path('register/', user_views.Register.as_view()),
    path('pandas_request/', user_views.PandasResult.as_view()),
    path("", user_views.login_render)
]