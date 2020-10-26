"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from api.views import SystemAdminAuthenticationView, SystemAdminJWTAuthenticationView, SystemAdminCreateAccountView, SystemAdminDeleteAccountView
from shop_environ import API_VERSION

API_URL = f"api/{API_VERSION}"

urlpatterns = [
    path('admin/', admin.site.urls),
    # add
    path('api/', include('api.urls')),
    path(f"{API_URL}/Admin-login/", SystemAdminAuthenticationView.as_view()),
    path(f"{API_URL}/Admin-auth/", SystemAdminJWTAuthenticationView.as_view()),
    path(f"{API_URL}/Admin-create-account/", SystemAdminCreateAccountView.as_view()),
    path(f"{API_URL}/Admin-delete-account/", SystemAdminDeleteAccountView.as_view())
]
