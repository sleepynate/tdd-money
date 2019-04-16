from Money import Money


class Dollar(Money):

    def times(self, n):
        return Dollar(self.amount * n)

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return "Dollar(" + str(self.amount) + ")"
