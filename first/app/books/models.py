from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=100, verbose_name="Название книги")
