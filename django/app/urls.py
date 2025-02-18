from django.urls import path
from app import views

urlpatterns = [
    path("addpeople", views.add, name="add"),
    path("/insert",views.insert,name="insert"),
    path("removepeople",views.remove,name="removepeople"),
    path("/delete",views.delete,name="delete"),
    path("search",views.search,name="search"),
    path("/show",views.show,name="show"),
    path("/showpeople/<int:id>",views.showpeople,name="showpeople"),
    path("",views.home,name="home"),
    path("/addpeople",views.add,name="addpeople"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("/home",views.home,name="home")
]