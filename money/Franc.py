from Money import Money


class Franc(Money):

    def times(self, n):
        return Franc(self.amount * n)

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return "Franc(" + str(self.amount) + ")"
