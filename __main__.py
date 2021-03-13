import use_cases
import presenter


if __name__ == "__main__":
    view = presenter.ConsoleView()
    presenter = presenter.Presenter(view=view)
    random_gen = use_cases.RandomGenerator()
    play_simon = use_cases.Play(i_presenter=presenter,
                                i_number_generator=random_gen)
    play_simon.run()
