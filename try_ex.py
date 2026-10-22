import math

def is_finite_number(value):
    if not is_number(value):
        return False
    return math.isfinite(value)

def is_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    return True

def is_valid_amount(amount):
    if not is_finite_number(amount) or amount <= 0:
        return False
    return True

def validate_amount(amount):
    if not is_number(amount):
        raise TypeError("Сумма должна быть числом")
    if not is_finite_number(amount):
        raise ValueError("Сумма должна быть конечным числом")
    if amount <= 0:
        raise ValueError("Сумма должна быть больше нуля")
    return amount

def is_valid_balance(balance):
    if not is_finite_number(balance) or balance < 0:
        return False
    return True

def can_transfer(balance, amount):
    if is_valid_balance(balance) and is_valid_amount(amount):
        return balance >= amount
    return False

def make_transfer(balance, amount):
    if not is_number(balance):
        raise TypeError("Баланс должен быть числом")

    if not is_number(amount):
        raise TypeError("Сумма должна быть числом")

    if not math.isfinite(amount):
        raise ValueError("Сумма должна быть конечным числом")

    if balance < 0:
        raise ValueError("Баланс не может быть отрицательным")

    if amount <= 0:
        raise ValueError("Сумма должна быть больше нуля")

    if not can_transfer(balance, amount):
        raise ValueError("Недостаточно средств")
    return balance - amount

#make_transfer(100, float("-inf"))
#make_transfer(100, float("nan"))


