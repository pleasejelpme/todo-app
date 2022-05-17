from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, AppLoginView, AppRegisterView

urlpatterns = [
    path('login/', AppLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='list'), name='logout'),
    path('register/', AppRegisterView.as_view(), name='register'),

    path('', TaskList.as_view(), name='list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('add-task/', TaskCreate.as_view(), name='create'), 
] 