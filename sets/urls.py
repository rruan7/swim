from django.urls import path
from . import views

urlpatterns = [
    # link root app URL to set_index view
    path("", views.set_generator, name="set_generator"),
    path("display", views.set_index, name="set_index"),
    path("<int:pk>/", views.set_detail, name="set_detail"),
]