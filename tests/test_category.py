import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestCategory(unittest.TestCase):
    def test_search_by_category(self):
        items = [DigitalVideoDisc("The Lion King", "Animation"),
                 DigitalVideoDisc("Star Wars", "Science Fiction")]
        result = search_by_category(items, "Animation")
        self.assertEqual([d.title for d in result], ["The Lion King"])