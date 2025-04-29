class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self  # Връща самия итерируем обект

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

fibs = Fibs()

for f in fibs:
    if f > 1000:   #Връща първото число на Фибоначи, по-голямо от 1000
        print(f)
        break
