from service import library_service

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Issued Details")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library_service.show_books()

    elif choice == "2":
        library_service.issue_book()

    elif choice == "3":
        library_service.return_book()

    elif choice == "4":
        library_service.issued_details()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")