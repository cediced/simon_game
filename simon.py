class Simon:
    def __init__(self):
        self.set_activated = False
        self.set_number = 0
        self.index_in_set = -1
        self.is_lost = False
        self.numbers = []
        self.number_min = 1
        self.number_max = 4

    @property
    def number_max(self):
        return self._number_max

    @number_max.setter
    def number_max(self, value):
        if value < 10:
            self._number_max = value
        else:
            raise MaxNumberError(f"number max {value} higher than 9")

    def push(self, number):
        if self.set_activated:
            raise SetAlreadyActivatedError

        self.set_number += 1
        self.set_activated = True

        if number > self.number_max:
            raise MaxNumberError(f"number max {number} higher than {self.number_max}")

        self.numbers.append(number)

    def chose(self, number):

        if not self.set_activated:
            raise TooManyChoseForSetError

        self.index_in_set += 1

        if not number == self.numbers[self.index_in_set]:
            self.is_lost = True

        # detect end of the set if chosen numbers == nb of the set
        if self.set_number == self.index_in_set + 1:
            self.index_in_set = -1
            self.set_activated = False


class MaxNumberError(Exception):
    """
    if the the chosen number is above the
    allowed maximum
    """


class TooManyChoseForSetError(Exception):
    """
    for set 1 -> the user should only chose 1 number
    for set 2 -> 2 times

    if the rule is not respected the Error is raised
    """


class SetAlreadyActivatedError(Exception):
    """
    we can only pus a number once per set, raise if not respected
    """

