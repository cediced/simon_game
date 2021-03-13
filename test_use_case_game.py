import use_cases


class DummyPresenter(use_cases.IPresenter):
    def __init__(self, data_to_return):
        self.index = 0
        self.data_to_return = data_to_return
        self.get_user_input_called = 0
        self.print_number_to_find = 0
        self.print_losing_message = 0

    def get_user_input(self):
        self.get_user_input_called += 1
        try:
            result = self.data_to_return[self.index]
            self.index += 1
            return result
        except TypeError:
            return self.data_to_return

    def present_number_to_find(self, number):
        self.print_number_to_find += 1

    def present_losing_message(self, set_number):
        self.print_losing_message += 1


class RandomGenerator(use_cases.IRandomGenerator):
    def __init__(self, datas):
        self.index = -1
        self.datas = datas

    def generate_int(self):
        self.index += 1
        return self.datas[self.index]


def test_loses_set_one():
    generator = RandomGenerator([1])
    presenter = DummyPresenter(data_to_return=2)
    usecase_play = use_cases.Play(i_presenter=presenter,
                                  i_number_generator=generator)
    usecase_play.run()
    assert usecase_play.response_model == {"set": 1}


def test_loses_at_set_2():
    generator = RandomGenerator([1, 2])
    presenter = DummyPresenter(data_to_return=[1, 1, 3])

    usecase_play = use_cases.Play(i_presenter=presenter,
                                  i_number_generator=generator)

    usecase_play.run()
    assert usecase_play.response_model == {"set": 2}


def test_loses_at_set_3():
    generator = RandomGenerator([1, 2, 3])
    presenter = DummyPresenter(data_to_return=[1, 1, 2, 4])

    usecase_play = use_cases.Play(i_presenter=presenter,
                                  i_number_generator=generator)

    usecase_play.run()
    assert usecase_play.response_model == {"set": 3}

