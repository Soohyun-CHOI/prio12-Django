from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list),
    path("<int:pk>/", views.post_read, name="post-read"),
    path("create/", views.post_create, name="post-create"),
]