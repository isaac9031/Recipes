from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm, PostForm
from django.contrib.auth.decorators import login_required




# Create your views here.
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context={
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)

#goes with Recipe
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list" : recipes,
    }
    return render(request, "recipes/list.html", context)

@login_required
def create_recipe(request):
    if request.method == "POST": #used when the person submits the form by clicking Create button
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list") #uses the urlpattern name = "recipe_list" to redirect to the recipe_list view
    else: #will pop up on the browser when somone clicks a link to only see the page - "GET"
        form = RecipeForm()

    context = {
        "form": form,
    }
    return render(request, "recipes/create.html", context)  #render: render is a function provided by Django for rendering HTML templates. It
                                                        # takes care of loading the specified HTML template, populating it with data from
                                                        # the context dictionary, and returning the rendered HTML as an HTTP response.



def edit_recipe(request, id):
    post = get_object_or_404(Recipe, id = id) #gets the object/id that we want to edit
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # POST is when the person has submitted the form
        if form.is_valid():
            form.save()             #creates form and save
            return redirect("show_recipe", id=id) #redirects to the recipe
    else:
        form = PostForm(instance=post)        #instance argument. The Django model form class uses that to figure out what's changed.

    context = {
        "post_form": form,
        "post_object": post,
    }
    return render(request, "recipes/edit.html", context)

@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author = request.user) #using query .filter to get only the recipes that the user made
    context = {
        "recipe_list" : recipes,
    }
    return render(request, "recipes/list.html", context)
