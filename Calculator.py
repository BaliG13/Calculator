def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "error"
    else:
        return (num1 / num2)


def sqroot(num1, num2):
    return num1 ** num2