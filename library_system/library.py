import json
import os
from library_system.book import Book
from library_system.member import Member

class Library:
    def __init__(self):
        self.books={}
        self.members={}
        
    def add_book(self, book):
        self.books[book.isbn]=book
        
    def find_book(self,keyword):
        return [
            book for book in self.books.values()
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
            or keyword == book.isbn
        ]
        
    def register_member(self, member):
        self.members[member.member_id] = member
        
    def borrow_book(self,member_id,isbn):
        member=self.members.get(member_id)
        book=self.books.get(isbn)
        
        if not member or not book:
            return "Invalid member or book!"
        
        if not book.available:
            return "Book already borrowed!"
        
        if not member.borrow_book(isbn):
            return "Borrow limit reached!"
        
        success, msg=book.check_out(member_id)
        return msg
    
    def return_book(self, member_id,isbn):
        member=self.members.get(member_id)
        book=self.books.get(isbn)
        
        if not member or not book:
            return "Invalid member or book!"
        
        if member.return_book(isbn):
            success, msg = book.return_book()
            return msg
        return "Return Failed!"
    
    def save_data(self):
        os.makedirs("data/backup", exist_ok=True)
        
        with open("data/books.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)
        with open("data/members.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)
            
    def load_data(self):
        if os.path.exists("data/books.json"):
            with open("data/books.json", "r") as f:
                data=json.load(f)
                for isbn, info in data.items():
                    self.books[isbn] = Book.from_dict(info)
                    
        if os.path.exists("data/members.json"):
            with open("data/members.json", "r") as f:
                data=json.load(f)
                for mid, info in data.items():
                    self.members[mid] = Member.from_dict(info)

    def view_all_books(self):
        if not self.books:
            return "No books available in the library!"
        
        book_list=[]
        for book in self.books.values():
            book_list.append(str(book))
        return "\n".join(book_list)
    
    def view_all_members(self):
        if not self.members:
            return "No members registered in the library!"
        
        member_list=[]
        for member in self.members.values():
            member_list.append(str(member))
            
        return "\n".join(member_list)
    
    def view_overdue_books(self):
        overdue_books=[book for book in self.books.values() if book.is_overdue()]
        
        if not overdue_books:
            return "No overdue books!"
        
        output=[]
        for book in overdue_books:
            output.append(
                f"{book.title} | ISBN: {book.isbn} | Borrowed By: {book.borrowed_by} | "
                f"Due Date: {book.due_date} | Days Overdue: {book.days_overdue()}"
            )
        return "\n".join(output)