from graphene_django import DjangoObjectType
from book_app.models import Author, Book

import graphene


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("name", "books", "id")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("name", "author", "id")


class AddBookMutation(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        name = graphene.String(required=True)
        author_name = graphene.String(required=True)

    def mutate(self, info, name, author_name):
        author = Author.objects.get_or_create(name=author_name)[0]
        book = Book.objects.create(author=author, name=name)
        return AddBookMutation(book=book)


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    authors = graphene.List(AuthorType)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()


class Mutation(graphene.ObjectType):
    add_book = AddBookMutation.Field()


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query, mutation=Mutation)
