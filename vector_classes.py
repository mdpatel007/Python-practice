## This code defines two classes for representing vectors in 2D and 3D space.
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is: {self.i}i + ,{self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is i: {self.i}, j: {self.j}, k: {self.k}")


# Example usagea 
a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show()