class Set:
    """A set is a weight and reps"""
    reps = None
    weight = None

    def __init__(self, weight, reps):
        self.weight = weight
        self.reps = reps

    def __str__(self):
        return self.weight + "x" + self.reps


class Exercise:
    """ Represents a single exercise with all sets """
    name = None
    date = None
    sets = []

    def __init__(self, name, date):
        self.sets = []
        self.name = name
        self.date = date

    def add_set(self, weight, reps):
        self.sets.append(Set(weight, reps))

    def __str__(self):
        set_str = ""
        for set in self.sets:
            set_str += str(set)
            set_str += " "

        return f"{self.date}: {self.name} - {set_str}"