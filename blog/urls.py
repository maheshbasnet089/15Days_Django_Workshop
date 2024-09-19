from django.urls import path
from .views.main_view import home,create_blog,single_blog,edit_blog
from .views.auth_view import register,login

urlpatterns = [
    path("",home), 
    path("register/",register), 
    path("login/",login), 
    path("create/",create_blog), 
    path("single/",single_blog), 
    path("edit/",edit_blog)
]
