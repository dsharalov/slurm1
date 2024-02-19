
import pytest
#import monkeypatch
from homework4 import get_random_target, compare_answer, main


def test_random():
    for test in range(1,10000):
        test = get_random_target()
#        print(test)
        result = (0 <= test and test <= 100)
        assert result == True

def test_comparison():
    assert compare_answer(50,80) == "TARGET IS MORE"
    assert compare_answer(90,80) == "TARGET IS LESS"
    assert compare_answer(80,80)  == "YOU WIN"


class InputMock:
    def __init__(self, inputs):
        self.inputs = iter(inputs)

    def __call__(self, *args, **kwargs):
        return next(self.inputs)

def test_main_game_result_win(monkeypatch, capsys):
    inputs = ["50"]
    input_mock = InputMock(inputs)

    with monkeypatch.context() as m:
        m.setattr('builtins.input', input_mock)
        main(target=50)
    captured = capsys.readouterr()
    assert "YOU WIN" in captured.out

def test_main_game_result_lose(monkeypatch, capsys):
    inputs = ["50"]
    input_mock = InputMock(inputs)

    with monkeypatch.context() as m:
        m.setattr('builtins.input', input_mock)
        main(target=60, tries=1)
    captured = capsys.readouterr()
    assert "YOU LOSE" in captured.out

