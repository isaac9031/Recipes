from django.urls import path
from recipes.views import recipe_list, show_recipe, create_recipe, edit_recipe

urlpatterns =[
    path("<int:id>/", show_recipe, name = "show_recipe"),
    path("", recipe_list, name= "recipe_list"),
    path("create/", create_recipe, name="create_recipe"),
    path("edit/<int:id>/", edit_recipe, name= "edit_recipe"),
]

# OLD WAY
# urlpatterns =[
#     path("recipes/<int:id>/", show_recipe, name = "show_recipe"),
#     path("recipes/", recipe_list, name= "recipe_list"),
#     path("recipes/create/", create_recipe, name="create_recipe"),
#     path("recipes/edit/<int:id>/", edit_recipe, name= "edit_recipe"),
# ]
