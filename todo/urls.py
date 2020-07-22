"""todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import (TodoListView, TodoCreateView,
                    TodoDeleteView, TodoUpdateView, CompleteToDo, UserFormView,
                    UserLoginView,
                    UserLogoutView, TodayTasksView, WeeklyTasks)

app_name = 'todosApp'

urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('today/', TodayTasksView.as_view(), name='today-tasks'),
    path('add-to-do/', TodoCreateView.as_view(), name='add-to-do'),
    path('<pk>/delete-to-do/', TodoDeleteView.as_view(), name='delete-to-do'),

    path('<pk>/update-to-do/', TodoUpdateView.as_view(), name='update-to-do'),

    path('<pk>/completed-task/', CompleteToDo.as_view(), name='to-do-completed'),

    path('user-registration/', UserFormView.as_view(), name='user-rgstr'),

    path('login/', UserLoginView.as_view(), name='login'),

    path('logout/', UserLogoutView.as_view(), name='logout'),

    # path('<int:year>/week/<int:week>/',
    #      WeeklyTasks.as_view(),
    #      name="weekly_tasks"),
]
