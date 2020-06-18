from django.views.generic import (ListView,
                                  CreateView, UpdateView, DeleteView, RedirectView,
                                  View)
from django.contrib.auth.views import (LogoutView,
                                       LoginView)
from .models import ToDo
from .forms import (MyUserForm)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import (SuccessMessageMixin)
from django.contrib.auth import authenticate, login
# Create your views here.


class CompleteToDo(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        todo_obj = get_object_or_404(ToDo, pk=kwargs['pk'])
        if todo_obj.is_completed:
            todo_obj.is_completed = False
            todo_obj.save()
        else:
            todo_obj.is_completed = True
            todo_obj.save()
        return reverse_lazy('todosApp:index')


class TodoCreateView(SuccessMessageMixin, CreateView):
    model = ToDo
    template_name = "create_todo.html"
    fields = ['title', 'todoDate', 'todoNote']
    success_url = reverse_lazy('todosApp:index')
    success_message = " %(title)s  was added to your tasks"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class UserLogoutView(LogoutView):
    template_name = 'logged_out.html'
    next_page = reverse_lazy('todosApp:login')


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserFormView(View):
    form_class = MyUserForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.email = email
            user.set_password(password)
            user.save()

            user = authenticate(email=email, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('todosApp:index')

        return render(request, self.template_name, {'form': form})
