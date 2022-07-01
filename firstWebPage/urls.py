"""firstWebPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from articles.views import detail_view,search_view,create_view
from firstWebPage import views

from accounts.views import login_view,logout_view,register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('article/<int:id>/', detail_view),
    path('article/', search_view),
    path('article/create/', create_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view)
]
