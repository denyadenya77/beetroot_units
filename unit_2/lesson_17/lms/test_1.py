from unit_2.lesson_17.lms.car_game import Car
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car_1 = Car(20)

    def test_move_left(self):
        self.car_1.move_left()
        self.assertEqual(self.car_1.direction, 'left')
        self.assertEqual(self.car_1.position, [-20, 0])

    def test_move_right(self):
        self.car_1.move_right()
        self.assertEqual(self.car_1.direction, 'right')
        self.assertEqual(self.car_1.position, [20, 0])

    def test_move_up(self):
        self.car_1.move_up()
        self.assertEqual(self.car_1.direction, 'up')
        self.assertEqual(self.car_1.position, [0, 20])

    def test_move_down(self):
        self.car_1.move_down()
        self.assertEqual(self.car_1.direction, 'down')
        self.assertEqual(self.car_1.position, [0, -20])

    def test_change_speed(self):
        self.car_1.change_speed(30)
        self.assertEqual(self.car_1.speed, 30)


if __name__ == '__main__':
    unittest.main()