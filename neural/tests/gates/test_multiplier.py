import unittest

from gates.multiplier import Multiplier

class TestMultiplier(unittest.TestCase):
    def test_single_forward(self):
        gate = Multiplier()
        z = gate.forward(3,4)
        self.assertEqual(12, z)
        self.assertEqual(3, gate.x)
        self.assertEqual(4, gate.y)

    def test_multiple_forward(self):
        gate = Multiplier()

        z = gate.forward(2,5)
        self.assertEqual(10, z)
        self.assertEqual(2, gate.x)
        self.assertEqual(5, gate.y)

        z = gate.forward(1,7)
        self.assertEqual(7, z)
        self.assertEqual(1, gate.x)
        self.assertEqual(7, gate.y)

    def test_single_backward(self):
        gate = Multiplier()
        gate.forward(3,4)
        g = gate.backward(2)

        self.assertEqual([8, 6], g)
    
    def test_two_instances(self):
        gate1 = Multiplier()
        gate2 = Multiplier()

        z1 = gate1.forward(4,5)
        z2 = gate2.forward(2,3)
        self.assertEqual(20, z1)
        self.assertEqual(6, z2)

        g1 = gate1.backward(3)
        g2 = gate2.backward(1)
        self.assertEqual([15, 12], g1)
        self.assertEqual([3, 2], g2)

if __name__ == '__main__':
    unittest.main()