from django.views.generic import (ListView,
                                  CreateView, UpdateView, DeleteView, RedirectView)
from .models import ToDo
# from .forms import (ToDoForm)
from django.shortcuts import (get_object_or_404)
from django.urls import reverse_lazy
from django.contrib.messages.views import (SuccessMessageMixin)
# Create your views here.


class CompleteToDo(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        todo_obj = get_object_or_404(ToDo, pk=kwargs['pk'])
        todo_obj.is_completed = True
        todo_obj.save()
        # if todo_obj.is_completed:
        #     print('It has been completed')
        # else:
        #     print('Not completed')
        #     todo_obj.is_completed = True
        return reverse_lazy('todosApp:index')


class TodoCreateView(CreateView):
    model = ToDo
    template_name = "create_todo.html"
    fields = ['title', 'todoDate', 'todoNote']
    success_url = reverse_lazy('todosApp:index')


class TodoDeleteView(SuccessMessageMixin, DeleteView):
    model = ToDo
    template_name = "delete_todo.html"
    success_url = reverse_lazy('todosApp:index')
    success_message = "To-Do was created successfully"


class TodoUpdateView(UpdateView):
    model = ToDo
    template_name = "update_todo.html"
    fields = ['title', 'todoDate', 'todoNote']


class TodoListView(ListView):
    model = ToDo
    template_name = "todo_list.html"
    context_object_name = 'chores'
