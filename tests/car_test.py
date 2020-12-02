from src.sample.car import *
import unittest
from unittest.mock import *


class CarTest(unittest.TestCase):

    def test_needsFuel_yes(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        self.assertEqual(car.needsFuel(), True)

    def test_needsFuel_no(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        self.assertEqual(car.needsFuel(), False)

    def test_getEngineTemperature(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 100
        self.assertEqual(car.getEngineTemperature(), 100)

    def test_driveTo(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = 'jedziemy do Wejherowo'
        self.assertEqual(car.driveTo('Wejherowo'), 'jedziemy do Wejherowo')


if __name__ == '__main__':
    unittest.main()