from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d')
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_date']


class Category(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'








