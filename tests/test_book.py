import unittest
from library_system.book import Book

class TestBook(unittest.TestCase):
    def test_checkout(self):
        book = Book("Python", "Guido", "123", 2024)
        success, _ = book.check_out("M1")
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()