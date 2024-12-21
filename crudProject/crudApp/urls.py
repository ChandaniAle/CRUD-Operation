from django.urls import path
from .views import *
# from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("form/", form, name="form"),
    path("about/", about, name="about"),
    path("delete_data/<int:id>",delete_data, name="delete_data"),
    path("edit/<int:id>", edit, name="edit"),
    path("search/", search_form,name="search_form")

]
