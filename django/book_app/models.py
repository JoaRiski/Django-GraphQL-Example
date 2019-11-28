from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="books"
    )

    def __str__(self):
        return self.name
