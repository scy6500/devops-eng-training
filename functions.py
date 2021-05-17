import math


def check_num(num):
    if num.isdigit():
        return True
    else:
        return False


# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기
def add_function(num1, num2):
    if check_num(num1) and check_num(num2):
        result = int(num1) + int(num2)
    else:
        result = "check parameter"
    return result


def subtract_function(num1, num2):
    if check_num(num1) and check_num(num2):
        result = int(num1) - int(num2)
    else:
        result = "check parameter"
    return result


def multiply_function(num1, num2):
    if check_num(num1) and check_num(num2):
        result = int(num1) * int(num2)
    else:
        result = "check parameter"
    return result


def division_function(num1, num2):
    if check_num(num1) and check_num(num2):
        result = int(num1) // int(num2)
    else:
        result = "check parameter"
    return result


def sqrt_function(num):
    if check_num(num):
        result = math.sqrt(int(num))
    else:
        result = "check parameter"
    return result
