class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):

        if self.i == 0:
            return {self.start}
        if self.i == 1:
            return {self.end}
        raise StopIteration()




en = EvenNumbers(10, 25)
print(en)
for i in en:
    print(i)