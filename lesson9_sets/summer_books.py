home_library = set()
summer_books = set()

num_of_lib = int(input('Enter the number of books in library: '))
num_of_books = int(input('Enter the number of summer books: '))

print('Enter your home books: ')
for library in range(1, num_of_lib + 1):
    book = input()
    book = book.title()
    home_library.add(book)
print('Enter your summer books: ')
for books in range(1, num_of_books + 1):
    book = input()
    book = book.title()
    summer_books.add(book)

inter = home_library.intersection(summer_books)
if inter:
    print(inter, '- yes')
else:
    print('No duplicate books.')
