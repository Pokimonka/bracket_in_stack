import pytest

from stack import check_brackets


@pytest.mark.parametrize(
    'brackets',
    (
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
    )
)
def test_check_brackets_true(brackets):
    assert check_brackets(brackets) == True


@pytest.mark.parametrize(
    'brackets',
    (
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    '}{'
    )
)
def test_check_brackets_false(brackets):
    assert check_brackets(brackets) == False


