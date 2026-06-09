from models import library_data

print("FILE:", library_data.__file__)
print("BOOKS:", hasattr(library_data, "books"))
print(dir(library_data))
def show_books():
    print("\nAvailable Books:")

    for book, status in library_data.books.items():
        if status:
            print(book)


def issue_book():
    book = input("Enter Book Name: ")

    if book in library_data.books and library_data.books[book]:

        student = input("Student Name: ")
        days = int(input("Issued for how many days: "))

        library_data.books[book] = False

        library_data.issued_books[book] = {
            "student": student,
            "days": days
        }

        print("Book Issued Successfully")

    else:
        print("Book Not Available")


def return_book():
    book = input("Enter Book Name: ")

    if book in library_data.issued_books:

        used_days = int(input("How many days did you keep the book? "))

        allowed_days = library_data.issued_books[book]["days"]

        fine = 0

        if used_days > allowed_days:

            extra = used_days - allowed_days

            if extra <= 7:
                fine = extra * 10

            elif extra <= 14:
                fine = extra * 20

            else:
                fine = extra * 60

        print("Fine = Rs.", fine)

        library_data.books[book] = True
        del library_data.issued_books[book]

        print("Book Returned Successfully")

    else:
        print("Book was not issued")


def issued_details():
    print("\nIssued Books:")

    if not library_data.issued_books:
        print("No books issued")

    else:
        for book, data in library_data.issued_books.items():
            print(book, "->", data)