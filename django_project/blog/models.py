from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField()
    #author: 추후 작성 예정

    def __str__(self): #자바에서는 toString과 같음
        return f'[{self.pk}] {self.title}'