import os
import random

from abc import ABC

import simon


class IPresenter(ABC):
    def get_user_input(self):
        raise NotImplementedError

    def present_number_to_find(self, number):
        raise NotImplementedError

    def present_losing_message(self, set_number):
        raise NotImplementedError


class IRandomGenerator(ABC):
    def generate_int(self):
        raise NotImplementedError


class RandomGenerator(IRandomGenerator):
    def __init_(self):
        pass

    def generate_int(self):
        return random.randint(1, 4)


class Play:
    def __init__(self, i_presenter: IPresenter,
                 i_number_generator: IRandomGenerator):

        self.presenter = i_presenter
        self.number_generator = i_number_generator
        self.response_model = {}

    def run(self):
        game = simon.Simon()

        while not game.is_lost:
            number = self.number_generator.generate_int()  # I/O
            self.presenter.present_number_to_find(number)
            game.push(number)

            for i in range(0, game.set_number):
                chosen = self.presenter.get_user_input()  # I/O
                game.chose(int(chosen))  # validation, interface, may change

                if game.is_lost:
                    self.presenter.present_losing_message(set_number=game.set_number)
                    break

        self.response_model = {"set": game.set_number}

