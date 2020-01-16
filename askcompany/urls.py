from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


# 원래는 Model
def mysum(request, x, y):
    result = x + y
    return HttpResponse(f"result = {result}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mysum/<int:x>/<int:y>", mysum)
]
