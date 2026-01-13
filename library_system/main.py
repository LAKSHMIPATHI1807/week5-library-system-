from library_system.library import Library,Book,Member

def main():
    library=Library()
    library.load_data()
    
    while True:
        print("-"*50)
        print("         LIBRARY MANAGEMENT SYSTEM")
        print("-"*50)
        print("\n1. Add New Book\n2. Register New Member\n3. Borrow Book\n4. Return Book\n5. Search Book\n6. View All books\n7. View All Members\n8. View Overdue Books\n9. Save & Exit\n0. Exit Without Saving")
        print()
        
        choice=input("Enter your choice: ")
        
        if choice=="1":
            library.add_book(Book(
                input("Title: "),
                input("Author: "),
                input("ISBN: "),
                input("Year: ")
            ))
            print("Book added!")
            
        elif choice=="2":
            library.register_member(Member(
                input("Name: "),
                input("Member ID: ")
            ))
            print("Member Registered!")
            
        elif choice=="3":
            print(library.borrow_book(input("Member ID: "), input("ISBN: ")))
            
        elif choice=="4":
            print(library.return_book(input("Member ID: "), input("ISBN: ")))
            
        elif choice=="5":
            for book in library.find_book(input("Search: ")):
                print(book)
                
        elif choice=="6":
            print("\n --- All Books in Library --- ")
            print(library.view_all_books())
            
        elif choice=="7":
            print("\n --- Library Members --- ")
            print(library.view_all_members())
            
        elif choice=="8":
            print("\n --- Overdue Books --- ")
            print(library.view_overdue_books())
            
        elif choice=="9":
            library.save_data()
            print("Data save successfully and Exiting Program!")
            break
        
        elif choice =="0":
            print("Exited the program successfully!")
            break
        
        else:
            print("Invalid choice!")
            
if __name__=="__main__":
    main()