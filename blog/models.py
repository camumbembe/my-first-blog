from django.db import models
from django.utils import timezone


class Post(models.Model): #definindo o objeto, nesse caso post. models.Model indica que é um modelo de django, para que o django saiba que deve armazená-lo no banco de dados
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(blank= True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title




