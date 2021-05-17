# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성
import pytest
import os.path
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)
import functions


def test_add():
    assert functions.add_function("6", "2") == 8
    assert functions.add_function("6", "string") == "check parameter"
    assert functions.add_function("string", "2") == "check parameter"
    assert functions.add_function("string", "string") == "check parameter"


def test_subtract():
    assert functions.subtract_function("6", "2") == 4
    assert functions.subtract_function("6", "string") == "check parameter"
    assert functions.subtract_function("string", "2") == "check parameter"
    assert functions.subtract_function("string", "string") == "check parameter"


def test_multiply():
    assert functions.multiply_function("6", "2") == 12
    assert functions.multiply_function("6", "string") == "check parameter"
    assert functions.multiply_function("string", "2") == "check parameter"
    assert functions.multiply_function("string", "string") == "check parameter"


def test_division():
    assert functions.division_function("6", "2") == 3
    assert functions.division_function("6", "string") == "check parameter"
    assert functions.division_function("string", "2") == "check parameter"
    assert functions.division_function("string", "string") == "check parameter"


def test_sqrt():
    assert functions.sqrt_function("4") == 2.0
    assert functions.sqrt_function("string") == "check parameter"

