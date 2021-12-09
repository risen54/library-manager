class Library:
	def __init__(self, list_of_books, lib_name):
		self.list_of_books = list_of_books
		self.lib_name = lib_name

	def display_books(self):
		print(self.list_of_books)

	def borrow(self, book_name):
		self.list_of_books.remove(book_name)
		print(f"Book {book_name} removed!")

	def donate_book(self, book_name):
		self.list_of_books.add(book_name)
		print("Book added!")

	def return_book(self, book_name):
		self.list_of_books.add(book_name)
		print("Book returned!")


def main(books, name):
	lib = Library(books, name)
	while True:
		print(f"-~=Welcome to {name}=~-")
		opt = int(input("""~Select an option~
1) Display books
2) Borrow book
3) Donate a book
4) Return book
Enter your option here: """))

		if opt == 1:
			lib.display_books()
			input()
		elif opt == 2:
			book_name = input("Enter book name:").lower()
			lib.borrow(book_name)
			input()
		elif opt == 3:
			book_name = input("Enter book name").lower()
			lib.donate_book(book_name)
			input()
		elif opt == 4:
			book_name = input("Enter book name: ").lower()
			lib.return_book(book_name)
			input()
		else:
			print("Option doesn't Exist! Try again.")
			input()


if __name__ == '__main__':
	myfav_books = ['20,000 leagues under the sea', 'life of pi', 'the way of kings']
	main(myfav_books, "Satvik's Library")
