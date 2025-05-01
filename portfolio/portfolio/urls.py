"""
URL configuration for portfolio project.

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
from project import views as project_view
from login import views as login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("project/list", project_view.show_list,name = 'project_list'),
    path("project/<int:project_id>",project_view.show_detail,name = 'project_detail'),
    path('project/create/', project_view.create_project, name='project_create'),
    path('project/<int:project_id>/edit/', project_view.edit_project, name='project_edit'),
    path('project/mine/', project_view.my_projects, name='my_projects'),


    path("login/page",login_view.show_page, name = 'login_page'),
    path("login/singup",login_view.signup, name = 'login_signup')
]
