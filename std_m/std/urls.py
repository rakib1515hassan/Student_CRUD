from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name= "home"),
    path("home/", home,name= "home"),
    path("base/", base,name= "base"),
    path("add-std/", add_std,name= "add_std"),
    path("delete-std/<int:id>", delete_std,name= "delete_std"),
    path("update-std/<int:id>", update_std,name= "update_std"),
    path("do-update-std/<int:id>", do_update_std,name= "do_update_std"),
    path("search/", search, name= "search"),
]