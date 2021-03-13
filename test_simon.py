import pytest
from simon import Simon, MaxNumberError, TooManyChoseForSetError, SetAlreadyActivatedError


@pytest.fixture
def game():
    return Simon()


def assert_winning(game):
    assert not game.is_lost


def assert_lost(game):
    assert game.is_lost


def test_game_is_initialized(game):
    assert 4 == game.number_max
    assert 1 == game.number_min
    assert 0 == game.set_number
    assert not game.is_lost
    assert len(game.numbers) == 0


def test_max_of_max_number_is_higher_9(game):
    with pytest.raises(MaxNumberError) as execinfo:
        game.number_max = 10

    assert f"number max {10} higher than 9"


def test_cannoot_push_number_higher_than_max(game):
    with pytest.raises(MaxNumberError) as execinfo:
        game.push(5)


def test_wrong_chosen_number_set_is_finished_and_the_game_is_lost(game):
    game.push(1)
    game.chose(2)
    assert game.is_lost


def test_if_chosen_number_right_then_set_is_finished_and_lost_is_false(game):
    game.push(1)
    game.chose(1)
    assert_winning(game)
    assert game.set_number == 1


def test_wins_second_set(game):
    game.push(1)
    game.chose(1)

    game.push(2)
    game.chose(1)
    game.chose(2)

    assert_winning(game)
    assert game.set_number == 2


def test_wins_second_set_after_first_chose(game):
    game.push(1)
    game.chose(1)

    game.push(2)
    game.chose(1)
    game.chose(2)

    assert_winning(game)
    assert game.set_number == 2


def test_wins_second_set_after_second_chose(game):
    game.push(3)
    game.chose(3)

    game.push(4)
    game.chose(3)
    game.chose(4)

    assert_winning(game)
    assert game.set_number == 2


def test_wins_3_sets(game):
    game.push(3)
    game.chose(3)

    game.push(4)
    game.chose(3)
    game.chose(4)

    game.push(1)
    game.chose(3)
    game.chose(4)
    game.chose(1)

    assert_winning(game)


def test_wins_4_sets(game):
    game.push(1)
    game.chose(1)

    game.push(2)
    game.chose(1)
    game.chose(2)

    game.push(3)
    game.chose(1)
    game.chose(2)
    game.chose(3)

    game.push(4)
    game.chose(1)
    game.chose(2)
    game.chose(3)
    game.chose(4)

    assert_winning(game)


def test_cannot_use_chose_more_than_1_at_the_first_set(game):
    game.push(1)
    game.chose(1)
    with pytest.raises(TooManyChoseForSetError):
        game.chose(1)


def test_cannot_use_chose_more_than_2_at_the_first_set(game):
    game.push(1)
    game.chose(1)

    game.push(2)
    game.chose(1)
    game.chose(2)
    with pytest.raises(TooManyChoseForSetError):
        game.chose(1)


def test_push_more_than_one_time_in_an_activated_set(game):
    game.push(1)
    with pytest.raises(SetAlreadyActivatedError):
        game.push(1)


def test_raise_if_push_in_the_2nd_activated_set(game):
    game.push(1)
    game.chose(1)

    game.push(2)
    game.chose(1)
    with pytest.raises(SetAlreadyActivatedError):
        game.push(1)

