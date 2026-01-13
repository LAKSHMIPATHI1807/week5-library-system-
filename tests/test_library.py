import unittest
from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

class TestLibrary(unittest.TestCase):
    def test_borrow_book(self):
        lib = Library()
        lib.add_book(Book("Python", "Guido", "123", 2024))
        lib.register_member(Member("Alice", "M1"))
        result = lib.borrow_book("M1", "123")
        self.assertIn("successfully", result)

if __name__ == "__main__":
    unittest.main()