"""petcare URL Configuration

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
from petcare import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexPage),
    path('admin/', admin.site.urls),
    # path('admin/', views.admin),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('user/',views.user),
    path('volunteer/', views.volunteer),
    path('login/', views.login),
    path('consult/', views.consult),
    path('adoption/', views.adoption),
    path('behaviour/', views.behaviour),
    path('care/', views.care),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('updatedetails/', views.updateDetails),
    path('contacts/', views.contacts),
    path('confirmation/<int:petid>', views.confirmation),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)