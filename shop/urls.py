from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("", views.item_list),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    path("new/", views.item_new)
]
