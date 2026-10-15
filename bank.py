
import math


def transfer(balance_from, balance_to, amount):
    values = (balance_from, balance_to, amount)

    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return balance_from, balance_to, False
        if not math.isfinite(value):
            return balance_from, balance_to, False

    if balance_from < 0 or balance_to < 0 or amount <= 0:
        return balance_from, balance_to, False

    if amount > balance_from:
        return balance_from, balance_to, False

    return balance_from - amount, balance_to + amount, True

def get_account_info(balance):
    if isinstance(balance, bool) or not isinstance(balance, (int, float)):
        return None

    if not math.isfinite(balance) or balance < 0:
        return None

    return f"Баланс счёта: {balance:.2f}"