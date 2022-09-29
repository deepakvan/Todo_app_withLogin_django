
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('complete/<int:id>', views.complete, name="completedid"),
    path('completed', views.completed, name="completed"),
    path('completed/delete/<int:id>', views.completed_delete, name="completed"),

    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout")

]
