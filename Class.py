class TriangleChecker:
    def __init__(self, number=None):
        if isinstance(number, int):
            self.number = number

    def is_triangle(self):
        if self.number:

