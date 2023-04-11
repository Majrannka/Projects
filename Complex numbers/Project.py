# Oprogramowanie matematyczne - projekt: Palka, Paszkiewicz

import math
import cmath


class Quadratic_poly:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return str(self.elements)

    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise ValueError('Scalar must be an integer or a float!')

        quotients = []
        for i in self.elements:
            quotients.append(i)

        new_quotients = [other * j for j in quotients]
        new_quadratic = tuple(new_quotients)
        return Quadratic_poly(new_quadratic)

    __rmul__ = __mul__

    def delta(self):
        if self.elements[0] == 0:
            raise ValueError("The entered coefficients "
                             "do not form a quadratic poly!")
        else:
            return self.elements[1]**2 \
                   - 4 * self.elements[0] * self.elements[2]

    def solve(self):
        a = self.elements[0]
        b = self.elements[1]

        if a == 0:
            raise ValueError("The entered coefficients "
                             "do not form a quadratic poly!")

        else:
            delta = self.delta()

            if delta > 0:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)

                solution = "The equation has two real solutions:" \
                           + str(x1) + " and " + str(x2)
                return solution
            elif delta == 0:
                solution = "The equation has one double solution:" \
                           + str(-b/(2*a))
                return solution
            else:
                x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                x2 = (-b - cmath.sqrt(delta)) / (2 * a)

                solution = "The equation has two complex solutions:" \
                           + str(x1) + " and " + str(x2)
                return solution

    def __str__(self):
        a = self.elements[0]
        b = self.elements[1]
        c = self.elements[2]

        if a == 0:
            raise ValueError("The entered coefficients "
                             "do not form a quadratic poly!")
        else:
            if a == 1:
                formula_a = "x\u00b2"
            elif a == -1:
                formula_a = "x\u00b2"
            else:
                formula_a = str(a) + "x\u00b2"

            if b == 1:
                formula_b = "+x"
            elif b == -1:
                formula_b = "-x"
            elif b == 0:
                formula_b = ""
            elif b > 0:
                formula_b = "+" + str(b) + "x"
            else:
                formula_b = "-" + str(abs(b)) + "x"

            if c == 0:
                formula_c = ""
            elif c > 0:
                formula_c = "+" + str(c)
            else:
                formula_c = "-" + str(abs(c))

            formula = formula_a + formula_b + formula_c
            return formula
