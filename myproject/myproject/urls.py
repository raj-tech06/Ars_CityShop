"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page
    path('shops/', views.shops, name='shops'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('superadmin-login/', views.superadmin_login, name='superadmin_login'),
    path('superadmin-panel/', views.superadmin_panel, name='superadmin_panel'),
    path('create-admin/', views.create_admin, name='create_admin'),
    path('view-admins/', views.view_admins, name='view_admins'),
    path('active-admins/', views.active_admins, name='active_admins'),
    path('superadmin-logout/', views.superadmin_logout, name='superadmin_logout'),

    # Admin Login & Dashboard
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),

    # after admin login
    path('add-product/', views.add_product, name='add_product'),
    path('selling-history/', views.selling_history, name='selling_history'),
    path('my-sales/', views.my_sales, name='my_sales'),
    path('manage-products/', views.manage_products, name='manage_products'),


    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),


]
