import unittest
from unit_2.lesson_17.presentation.pizza import Pizza, PIZZA_SMALL_SIZE, PIZZA_BIG_SIZE


class TestPizza(unittest.TestCase):

    def test_create_small_pizza(self):
        pizza = Pizza(PIZZA_SMALL_SIZE)
        self.assertEqual(pizza.size, 0)

    def test_create_big_pizza(self):
        pizza_1 = Pizza(PIZZA_BIG_SIZE)
        self.assertEqual(pizza_1.size, 1)

    def test_create_wrong_pizza(self):
        with self.assertRaises(TypeError):
            Pizza(3)

# class TestOrder(unittest.TestCase):






if __name__ == '__main__':
    unittest.main()