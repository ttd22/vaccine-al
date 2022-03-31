# """ This is the Calculator Class"""
# from calculator.operation import Addition, Subtraction, Multiplication
#
#
# class Calculator:
#     """ This is the default result property"""
#     result = 0
#
#     # def add(self, value_1):
#     #     self.result = self.result + value_1
#     #     return self.result
#
#     def add(self, value_1):
#         """ This is the add method"""
#         self.result = Addition.add(self.result, value_1)
#         return self.result
#
#     def subtract(self, value_1):
#         """ This is the subtract method"""
#         self.result = Subtraction.subtract(self.result, value_1)
#         return self.result
#
#     def multiply(self, value_1):
#         """ This is the multiply method"""
#         self.result = Multiplication.multiply(self.result, value_1)
#         return self.result
#
#     def get_result(self):
#         """ This is the get result method"""
#         return self.result


""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication


class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calculation = Subtraction.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the subtract method"""
        calculation = Multiplication.create(tuple_list)
        return calculation.get_result()

