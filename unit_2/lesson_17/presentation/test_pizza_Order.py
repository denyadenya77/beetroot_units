import unittest, logging
from unittest.mock import patch
from unit_2.lesson_17.presentation.pizza import Pizza, Order, PAYMENT_BY_CARD, PAYMENT_BY_CASH, PIZZA_SMALL_SIZE


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order_1 = Order()

    @patch.object(logging, 'debug')
    def test_select_pizza(self, mock_logging):
        # self.assertIsNone(self.order_1.pizza)
        self.order_1.select_pizza(PIZZA_SMALL_SIZE)
        mock_logging.assert_called_once_with("Set order pizza: small pizza")
        # self.assertIsNotNone(self.order_1.pizza)
        # self.assertEqual(self.order_1.pizza.size, PIZZA_SMALL_SIZE)
        # self.assertEqual(self.order_1.pizza.pizza_size, 'small size')



    # @patch.object(logging, 'debug')
    # def test_select_payment(self, mock_logging):
    #     self.order_1.select_payment(PAYMENT_BY_CASH)
    #     mock_logging.assert_called_once_with("Set order payment_method: cash")







    # @patch.object(logging, 'debug')
    # def test_confirm_order(self, mock_logging):
    #
    #     mock_logging.assert_called_once_with("Set order pizza: card")





if __name__ == '__main__':
    unittest.main()