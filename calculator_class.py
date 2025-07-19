# This is a simple calculator class that can compute the square, cube, and square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root is {self.n ** 0.5}")


# Example usage
a = Calculator(4)
a.square()
a.cube()
a.square_root()
