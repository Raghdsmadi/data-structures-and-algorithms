import pytest
from stack_queue_brackets.stack_brackets_q import Stack, validate_brackets

def test_backet1():
    value = '()'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected

def test_backet2():
    value = '(){}[]'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected


