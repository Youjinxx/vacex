from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/main/{self.pk}/'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:5]
# Create your models here.
