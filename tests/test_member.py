import unittest
from library_system.member import Member

class TestMember(unittest.TestCase):
    def test_borrow_limit(self):
        member = Member("Alice", "M1")
        for i in range(5):
            member.borrow_book(str(i))
        self.assertFalse(member.borrow_book("6"))

if __name__ == "__main__":
    unittest.main()