from django.urls import path
from recipes.views import recipe_list, show_recipe, create_recipe, edit_recipe, my_recipe_list

urlpatterns =[
    path("<int:id>/", show_recipe, name = "show_recipe"),
    path("", recipe_list, name= "recipe_list"),
    path("create/", create_recipe, name="create_recipe"), #name='create_recipe" is used in the url to redirect on create.html file. On views on create_recipe function after the form has been submitted,  the website redirects using "recipe_list"
    path("edit/<int:id>/", edit_recipe, name= "edit_recipe"),
    path("mine/", my_recipe_list, name = "my_recipe_list"),
]

# OLD WAY
# urlpatterns =[
#     path("recipes/<int:id>/", show_recipe, name = "show_recipe"),
#     path("recipes/", recipe_list, name= "recipe_list"),
#     path("recipes/create/", create_recipe, name="create_recipe"),
#     path("recipes/edit/<int:id>/", edit_recipe, name= "edit_recipe"),
# ]
