from django.db import models
from django.contrib import admin


class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.ManyToManyField(
        'Author',
        # on_delete=models.CASCADE,
        # verbose_name='Автор книги',
        # related_name='author_books'

    )
    description = models.TextField(verbose_name="Описание книги")
    id_publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        related_name='publishinghouse_books',
        verbose_name='ID Издательства',
        null=True,
        blank=True
    )
    date_creation = models.DateTimeField(verbose_name="Дата написании книги", null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления", null=True, blank=True)
    is_daleted = models.BooleanField(default=False, verbose_name="удалено")

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class PublishingHouse(models.Model):
    pub_house_name = models.CharField(max_length=300, verbose_name="Название издательство")
    pub_house_address = models.CharField(max_length=1500, verbose_name="Адрес издательства")
    pub_house_contact_phone = models.CharField(max_length=20, verbose_name="Номер телефона издательства")
    pub_house_email = models.EmailField(verbose_name="Название почты издательства")
    pub_house_site = models.URLField(verbose_name="Сайт издательства", null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_daleted = models.BooleanField(default=False, verbose_name="удалено")

    def __str__(self):
        return self.pub_house_name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Author(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    last_name = models.CharField(max_length=15, verbose_name="Фамилия")
    father_name = models.CharField(max_length=15, verbose_name="Отчество", null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name="Страна")
    birthday = models.DateField(max_length=8, verbose_name="Дата рождения")
    languages = models.JSONField(verbose_name='Язык на котором пишет автор', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_daleted = models.BooleanField(default=False, verbose_name="удалено")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class BookInline(admin.TabularInline):
    model = Book.author.through
