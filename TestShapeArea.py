# Юнит-тесты для класса с вычислением площади фигур ShapeArea из ShapeArea.py

import unittest
from ShapeArea import ShapeArea

class TestShapeArea(unittest.TestCase):
  # setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.shapeArea = ShapeArea()
  # Each test method starts with the keyword test_
  def test_triang(self):
    self.assertEqual(self.shapeArea.sTriang(7, 24, 25), 84) # Прямоугольный
    self.assertEqual(self.shapeArea.sTriang(-1, 24, 25), False) # С отрицательным значением
    self.assertEqual(self.shapeArea.sTriang(100, 2, 10), False)  # Не существующий
    self.assertEqual(self.shapeArea.sTriang(5, 5, 5), 10.83) # Правильный
    self.assertEqual(self.shapeArea.sTriang(7, 13, 7), 16.89) # Равнобедренный
    self.assertEqual(self.shapeArea.sTriang(9, 15, 7), 20.69)  # Треугольник
  def test_circ(self):
    self.assertEqual(self.shapeArea.sSirc(4), 50.27)
    self.assertEqual(self.shapeArea.sSirc(-1), 3.14)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()

