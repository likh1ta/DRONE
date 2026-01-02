import unittest
from autonomy.avoidance import Avoidance

class TestAutonomy(unittest.TestCase):
    def test_avoidance(self):
        avoidance = Avoidance(5.0)
        self.assertTrue(avoidance.check_obstacle(2.0))
        self.assertFalse(avoidance.check_obstacle(10.0))

if __name__ == '__main__':
    unittest.main()
