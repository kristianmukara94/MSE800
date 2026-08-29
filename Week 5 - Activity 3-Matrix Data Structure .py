# Week 5 - Activity 3: Matrix data structure

class Matrix:
    def __init__(self, data):
        self.data = data

    # multiply this matrix by another matrix (row . column for each cell)
    def multiply(self, other):
        return [[sum(a * b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data]


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[10, 11], [20, 21], [30, 31]])

print("Result:", m1.multiply(m2))
