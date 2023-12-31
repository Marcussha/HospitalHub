"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dj-admin', admin.site.urls),
    path('',include('authentication.urls')),
    path('roles/', include('roles.urls')),
    path('departments/', include('departments.urls')),
    path('services/', include('ministration.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('medicine/', include('medicine.urls')),
    path('customers/', include('customer.urls')),
    path('news/', include('news.urls')),
    path('authrole/', include('authrole.urls')),
    path('user/', include('user.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

