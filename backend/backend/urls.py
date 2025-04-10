"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import *

from django.conf import settings   # Application settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name='Homepage'),
    path('Dashboard/', Dashboard.as_view(), name='Dashboard'),
    path('trainer/', TrainerView.as_view(), name='TrainerView'),
    path('trainer/create/', CreateTrainer.as_view(), name='CreateTrainer'),
    path('register/', RegisterStudent.as_view(), name='RegisterStudent'),
    
    path('login', UserLoginView.as_view(), name = 'UserLoginView'),
    path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    
    path('courses/', CoursesView.as_view(), name='CoursesView'),
    
    #school
    path('StudentList/', StudentList.as_view(), name='StudentList'),
    path('class/list/', ClassList.as_view(), name='ClassList'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)