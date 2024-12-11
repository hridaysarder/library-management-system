class Library:
    book_list = []
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"The book has been borrowed")
        else:
            print(f"The book is already borrowed")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"The book has been returned")
        else:
            print(f"The book was not borrowed")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"ID: {self.__book_id}, Title: '{self.__title}', Author: {self.__author}, Availability: {availability_status}")

book1 = Book("101", "Message", "Mizanur Rahman Azhari")
book2 = Book("102", "Paradoxical Sazid", "Arif Azad")
book3 = Book("103", "Bela Forabar Agay", "Arif Azad")
book4 = Book("104", "Hobluder jonno programming", "Zhankar Mahbub")
book5 = Book("105", "Object Oriented Programming", "Hriday Sarder")

def menu():
    while True:
        print("Library Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            for book in Library.book_list:
                book.view_book_info()
        elif choice == '2':
            book_id = input("Enter the book ID: ")
            for book in Library.book_list:
                if book._Book__book_id == book_id:
                    book.borrow_book()
                    break
            else:
                print("Invalid book ID")
        elif choice == '3':
            book_id = input("Enter the book ID: ")
            for book in Library.book_list:
                if book._Book__book_id == book_id:
                    book.return_book()
                    break
            else:
                print("Invalid book ID")
        elif choice == '4':
            print("Exit menu")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    menu()
