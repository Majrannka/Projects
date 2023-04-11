# Oprogramowanie matematyczne - projekt: Palka, Paszkiewicz

import unittest
from Project import Quadratic_poly
from testfixtures import compare


class TestRootsOfUnity(unittest.TestCase):
    def test_types(self):
        eq_type = Quadratic_poly((0.1, 0.4, 0.3))
        self.assertIsInstance(eq_type.elements[0], (int, float),
                              "Coefficients must be of type int or float!")
        self.assertIsInstance(eq_type.elements[1], (int, float),
                              "Coefficients must be of type int or float!")
        self.assertIsInstance(eq_type.elements[2], (int, float),
                              "Coefficients must be of type int or float!")

    def test_mul(self):
        eq_mul1 = Quadratic_poly((1, 2, 1))
        eq_mul2 = Quadratic_poly((-2, 4, -7))
        compare(eq_mul1 * 4, Quadratic_poly((4, 8, 4)),
                suffix="The result of multiplication is not correct!")
        compare(-5 * eq_mul2, Quadratic_poly((10, -20, 35)),
                suffix="The result of multiplication is not correct!")

    def test_delta(self):
        eq_delta1 = Quadratic_poly((1, 2, 1))
        eq_delta2 = Quadratic_poly((1, 4, 3))
        eq_delta3 = Quadratic_poly((2, -2, 1))
        self.assertEqual(eq_delta1.delta(), 0,
                         "The discriminant is not correct!")
        self.assertEqual(eq_delta2.delta(), 4,
                         "The discriminant is not correct!")
        self.assertEqual(eq_delta3.delta(), -4,
                         "The discriminant is not correct!")

    def test_solve(self):
        eq_s1 = Quadratic_poly((1, 2, 1))
        eq_s2 = Quadratic_poly((1, 4, 3))
        eq_s3 = Quadratic_poly((2, -2, 1))
        self.assertEqual(eq_s1.solve(), "The equation has one double "
                                        "solution:" + str(-1.0),
                         "The equation is not solved correctly!")
        self.assertEqual(eq_s2.solve(), "The equation has two real "
                                        "solutions:" + str(-1.0) +
                                        " and " + str(-3.0),
                         "The equation is not solved correctly!")
        self.assertEqual(eq_s3.solve(), "The equation has two complex "
                                        "solutions:" + str(0.5+0.5j) +
                                        " and " + str(0.5-0.5j),
                         "The equation is not solved correctly!")

    def test_str(self):
        eq_str1 = Quadratic_poly((-1, 7, -6))
        eq_str2 = Quadratic_poly((1, 0, 9))
        self.assertEqual(eq_str1.__str__(), "x\u00b2+7x-6",
                         "The equation is not written correctly!")
        self.assertEqual(eq_str2.__str__(), "x\u00b2+9",
                         "The equation is not written correctly!")


if __name__ == '__main__':
    unittest.main()
