"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from allauth.account.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from rest_framework_swagger.views import get_swagger_view 

API_TITLE = 'Blog API' # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/rest-auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/v1/rest-auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/v1/rest-auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/v1/rest-auth/password/reset/confirm/', PasswordResetDoneView.as_view(), name='rest_password_reset_confirm'),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    #path('schema/', schema_view),#new
    path('swagger-docs/', schema_view)
    # Add other endpoints as needed
]










