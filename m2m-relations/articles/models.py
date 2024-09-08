from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    name = models.CharField(max_length=30)
    is_main = models.BooleanField(default=False)
    sections = models.ManyToManyField(Article,through="Relationship",related_name="tags")

    def __str__(self):
        return self.name
    
class Relationship(models.Model):
    tags = models.ForeignKey(Tags,on_delete=models.CASCADE,related_name="relationships")
    sections = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="relationship")


