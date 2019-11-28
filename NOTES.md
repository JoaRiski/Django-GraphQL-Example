Tools:
 * [GraphQL Voyager](https://apis.guru/graphql-voyager/)
 * [GraphQL Faker](https://github.com/APIs-guru/graphql-faker)

Outputting the schema

```bash
python manage.py graphql_schema
```

Queries:

```graphql
query GetBooks {
  books {
    name
    author {
      name
    }
  }
}
```

```graphql
mutation AddBook {
  addBook(authorName: "Joa Riski", name: "Another book") {
    book {
      name
      author {
        name
      }
    }
  }
}
```

```graphql
query GetBooksByAuthor {
  authors {
    name
    books {
      name
      id
    }
  }
}
```

```
query GetBooksByJoa {
  authors(name: "Joa Riski") {
    name
    books {
      name
    }
  }
}
```

```
query GetAwesomeBook2 {
  books(name: "Awesome book 2") {
    name
    id
    author {
      name
    }
  }
}
```


```
query getBooks($awesomeBookName: String!) {
  awesomeBooks: books(name: $awesomeBookName) {
    name
  }
  allBooks: books {
    name
  }
}

{
  "awesomeBookName": "Awesome book 2"
}
```
