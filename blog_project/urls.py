"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    re_path(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^api/v1/rest-auth/login/', include('rest_auth.registration.urls')),  # Include login
    re_path(r'^api/v1/rest-auth/logout/', include('rest_auth.registration.urls')),  # Include logout
    re_path(r'^api/v1/rest-auth/password/reset/', include('rest_auth.registration.urls')),  # Include password reset
    re_path(r'^api/v1/rest-auth/password/reset/confirm/', include('rest_auth.registration.urls')),  # Include password reset confirmation
    # Add other endpoints as needed
]






