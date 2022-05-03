import unittest
from evaluate_mathematical_expression import calc, Solver


class TestSolution(unittest.TestCase):
    def test_solve_addition(self):
        solver = Solver()
        self.assertEqual(solver.solve_addition("6+7"), "13")
        self.assertEqual(solver.solve_addition("-6+7"), "1")

    def test_solve_multiplication(self):
        solver = Solver()
        self.assertEqual(solver.solve_multiplication("6*7"), "42")
        self.assertEqual(solver.solve_multiplication("1*1"), "1")
        self.assertEqual(solver.solve_multiplication("6*7*8"), "336")
        self.assertEqual(solver.solve_multiplication("4*5+5*8"), "20+40")
        self.assertEqual(solver.solve_multiplication("-4*5"), "-20")
        self.assertEqual(solver.solve_multiplication("3*-8"), "-24")
        self.assertEqual(solver.solve_multiplication("-4*-5"), "20")

    def test_simple_testcases(self):
        solver = Solver()

        self.assertEqual("1 + 1", 2)
        self.assertEqual("8/16", 0.5)
        self.assertEqual("3 -(-1)", 4)
        self.assertEqual("2 + -2", 0)
        self.assertEqual("10- 2- -5", 13)
        self.assertEqual("(((10)))", 10)
        self.assertEqual("3 * 5", 15)
        self.assertEqual("-7 * -(6 / 3)", 14)
