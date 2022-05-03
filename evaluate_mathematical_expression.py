"""
https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python
"""
import re


class Solver:
    def solve(self, expression):
        expression = self.replace_whitespace(expression)

    def replace_whitespace(self, expression):
        new_expression = expression.replace(" ", "")
        return new_expression

    def solve_brackets(self, expression):
        new_expression = ""

        return new_expression

    def solve_addition(self, expression):
        new_expression = expression
        # TODO: don't filter "-"" in first group, it's currently part of .*
        pattern = r"(.*)(-?\d+\.*\d*)(\+)(-?\d+\.*\d*)(.*)"
        result = re.match(pattern, expression)
        if result:
            first_num = int(result[2])
            second_num = int(result[4])
            new_expression = result[1] + str(first_num + second_num) + result[5]
            new_expression = self.simplify_operands(new_expression)
            return self.solve_addition(new_expression)

        return new_expression

    def solve_multiplication(self, expression):
        new_expression = expression
        pattern = r"(.*)(-?\d+\.*\d*)(\*)(-?\d+\.*\d*)(.*)"
        result = re.match(pattern, expression)
        if result:
            first_num = int(result[2])
            second_num = int(result[4])
            new_expression = result[1] + str(first_num * second_num) + result[5]
            new_expression = self.simplify_operands(new_expression)
            return self.solve_multiplication(new_expression)

        return new_expression

    def solve_division(self, expression):
        pass

    def simplify_operands(self, expression):
        new_expression = (
            expression.replace("--", "").replace("+-", "-").replace("-+", "-")
        )
        return new_expression


def calc(expression):
    """
    self.assertEqual("1 + 1", 2)
    self.assertEqual("8/16", 0.5)
    self.assertEqual("3 -(-1)", 4)
    self.assertEqual("2 + -2", 0)
    self.assertEqual("10- 2- -5", 13)
    self.assertEqual("(((10)))", 10)
    self.assertEqual("3 * 5", 15)
    self.assertEqual("-7 * -(6 / 3)", 14)
    """
    return  # evaluated expression

