from abc import ABC
from use_cases import IPresenter


class View(ABC):
    def get_user_input(self, message):
        raise NotImplementedError

    def update_number_to_find(self, message):
        raise NotImplementedError

    def update_losing_message(self, message):
        raise NotImplementedError


class Presenter(IPresenter):
    def __init__(self, view: View):
        self.view_model = {"user_input_message": "chose the right number :",
                           "chosen_number_by_user": "",
                           "losing_message": ""}
        self.view = view

    def get_user_input(self):
        return self.view.get_user_input(self.view_model["user_input_message"])

    def present_number_to_find(self, number):
        self.view.update_number_to_find("next number " + str(number))

    def present_losing_message(self, set_number):
        self.view.update_losing_message(f"you lost!! you managed until set {set_number}")


class ConsoleView(View):
    def __init_(self, view_model):
        self.view_model = view_model

    def get_user_input(self, message):
        return input(message)

    def display(self, message):
        print(message)

    def update_number_to_find(self, message):
        self.display(message)

    def update_losing_message(self, message):
        self.display(message)
