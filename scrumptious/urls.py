"""scrumptious URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.shortcuts import redirect

def redirect_to_recipe_list(request):
    if request.method == "GET":
        return redirect("recipe_list") #it cames from urls in recipes, it used the name = recipe_list to get there



urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("", redirect_to_recipe_list , name="home_page"),
    path('admin/', admin.site.urls),
    path("recipes/", include("recipes.urls")),
]


#OLD WAY
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include("recipes.urls")),
# ]
