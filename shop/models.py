from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)  # 입력값 없어도 허용
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<{self.pk}> {self.name}"
