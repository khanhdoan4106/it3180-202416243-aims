import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=1.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("Extra", cost=1.0)))

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("B", cost=24.95))
        self.assertEqual(cart.total_cost(), 44.9)