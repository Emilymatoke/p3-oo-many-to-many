'''## Many to many relationships
Many objects in a certain class relate to other many objects in a another class.
- always involves a third table/class/ model ; contract class or join class or asscociation class- links the other two classes, creates an intermediary

Example ; BOOKS - one book can hold many authors
 AUTHORS - one author can have many books
 AUTHORSHIP -third entity to create relationship'''

class Book :
     book_count = 0

     def __init__(self, title) :
          self.title = title
          self.author = []
          Book.book_count += 1

     def add_author(self, author) :
          self.authors.append(author)
          author.books.append(self)




class Author :
     author_count = 0

     def __init__(self, name) :
          self.name = name
          self.book =[]
          Author.author_count += 1

     def write_book (self, book) :
          self.books.append(book)
          book.authors.append(self)

class Authorship :
     def __init__(self, book, author) :
          self.book = book
          self.author = author
          print(f"Authorship between {author.name} and {book.title}")          
          
     
          

             

