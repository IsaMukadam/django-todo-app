from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

def index(request):
    """
    Display the list of todo items and handle creation of new todos.

    - Retrieves all Todo items ordered by most recent date.
    - Handles POST requests to add new Todo items via a form.
    - Renders the 'todo/index.html' template with the list and form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered webpage with todo list and form.
    """
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    """
    Delete a specific todo item by its ID.

    - Retrieves the Todo item by the given `item_id`.
    - Deletes the item from the database.
    - Adds an informational message confirming deletion.
    - Redirects to the todo list page.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (str): The unique identifier of the Todo item to delete.

    Returns:
        HttpResponseRedirect: Redirects to the todo list view.
    """
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!")
    return redirect('todo')