from unittest import TestCase
from context import src
from  src import my_module
from src.my_module import Rover

cord="1,2"
ornt = "N"
rover = Rover(cord,ornt,(5,5))

class MyTest(TestCase):
    def test_add_one(self):
        """ test the add one method """
        result = my_module.addOne(2)
        self.assertEqual(result, 3)
        
    def test_grid(self):
        self.grid = "10,5"
        response = my_module.get_grid(self.grid)
        self.assertEqual(response,(10,5))

    def test_rotate_right(self):
        response = rover.rotate_right('N')
        self.assertEqual(response, ((1, 3), 'E'))

    def test_rotate_left(self):
        response = rover.rotate_left('N')
        self.assertEqual(response, ((1, 3), 'W'))

    def test_move_forward(self):
        response = rover.move_forward((1,2), 'N')
        self.assertEqual(response, ((1,3),'N'))

  