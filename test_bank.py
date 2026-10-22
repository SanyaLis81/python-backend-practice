

from bank import transfer


def test_successful_transfer():
    assert transfer(1000, 500, 300) == (700, 800, True)


def test_insufficient_funds():
    assert transfer(100, 500, 200) == (100, 500, False)


def test_zero_transfer():
    assert transfer(1000, 500, 0) == (1000, 500, False)


def test_string_amount():
    assert transfer(1000, 500, "100") == (1000, 500, False)


def test_nan_amount():
    assert transfer(1000, 500, float("nan")) == (1000, 500, False)


def test_negative_balance_tr():
    assert transfer(-1000, 500, 100) == (-1000, 500, False)


def test_transfer_entire_balance():
    balance_from, balance_to, success = transfer(1000, 500, 1000)
    assert balance_from == 0
    assert balance_to == 1500
    assert success is True

from bank import transfer, get_account_info
def test_get_account_info():
    assert get_account_info(1250) == "Баланс счёта: 1250.00"

def test_get_account_info_negative():
    assert get_account_info(-10) is None

def test_get_account_info_str():
    assert get_account_info("100") is None

import pytest
from try_ex import *

def test_negative_balance():
    with pytest.raises(ValueError, match="Баланс не может быть отрицательным"):
        make_transfer(-100, 50)

def test_string_balance():
    with pytest.raises(TypeError, match="Баланс должен быть числом"):
        make_transfer("abc", 50)
def test_bool_balance():
    with pytest.raises(TypeError, match="Баланс должен быть числом"):
        make_transfer(True, 50)
def test_insufficient_funds_transfer():
    with pytest.raises(ValueError, match="Недостаточно средств"):
        make_transfer(100, 200)
def test_successful_make_transfer():
    assert make_transfer(1000, 300) == 700
def test_transfer_entire_balance():
    assert make_transfer(500, 500) == 0
def test_nan_amount_transfer():
    with pytest.raises(ValueError, match="Сумма должна быть конечным числом"):
        make_transfer(100, float("nan"))
def test_inf_transfer():
    with pytest.raises(ValueError, match="Сумма должна быть конечным числом"):
        make_transfer(100, float("inf"))
def test_negative_infinity_amount_transfer():
    with pytest.raises(ValueError, match="Сумма должна быть конечным числом"):
        make_transfer(100, float("-inf"))
def test_zero_balance_transfer():
    with pytest.raises(ValueError, match="Недостаточно средств"):
        make_transfer(0, 50)
def test_zero_amount_transfer():
    with pytest.raises(ValueError, match="Сумма должна быть больше нуля"):
        make_transfer(100, 0)
def test_negative_amount_transfer():
    with pytest.raises(ValueError, match="Сумма должна быть больше нуля"):
        make_transfer(100, -50)
def test_string_amount_transfer():
    with pytest.raises(TypeError, match="Сумма должна быть числом"):
        make_transfer(100, "50")
def test_bool_amount_transfer():
    with pytest.raises(TypeError, match="Сумма должна быть числом"):
        make_transfer(100, True)
def test_bool_false_amount_transfer():
    with pytest.raises(TypeError, match="Сумма должна быть числом"):
        make_transfer(100, False)
def test_bool_none_amount_transfer():
    with pytest.raises(TypeError, match="Сумма должна быть числом"):
        make_transfer(100, None)
def test_is_finite_number_valid_int():
    assert is_finite_number(100) is True
    assert is_finite_number(float("nan")) is False
    assert is_finite_number("100") is False
def test_is_numberst():
    assert is_number(100) is True
    assert is_number(True) is False
    assert is_number("100") is False
def test_is_valid_amount():
    assert is_valid_amount(100) is True
    assert is_valid_amount(0) is False
    assert is_valid_amount(-50) is False
    assert is_valid_amount(float("inf")) is False
    assert is_valid_amount("100") is False
def test_can_transfer():
    assert can_transfer(1000, 300) is True
    assert can_transfer(100, 100) is True
    assert can_transfer(100, 200) is False
    assert can_transfer(-100, 50) is False
    assert can_transfer(100, 0) is False
@pytest.mark.parametrize(
    "amount, expected",
    [(25, True),
     (0, False),
     (-10, False),
     ("abc", False),
     (float("inf"),	False)
     ],
)
def test_amount(amount, expected):
    assert is_valid_amount(amount) is expected

@pytest.mark.parametrize(
    "balance, expected",
    [(100, True),
     (0, True),
     (-1, False),
     (float("nan"),	False)],
)
def test_balance(balance, expected):
    assert is_valid_balance(balance) is expected

@pytest.mark.parametrize(
    "balance, amount, expected",
    [
        (1000, 300,	True),
        (100, 100, True),
        (100, 200, False),
        (-100, 50, False),
        (100, 0, False)
    ],
)
def test_can_transfer(balance, amount, expected):
    assert can_transfer(balance, amount) is expected

def test_make_transfer():
    with pytest.raises(ValueError, match="Недостаточно средств"):
        make_transfer(100, 200)

@pytest.mark.parametrize(
    "balance, amount, message_error",
    [
        (-100, 50, "Баланс не может быть отрицательным"),
        (100, 200, "Недостаточно средств"),
        (100, 0, "Сумма должна быть больше нуля"),
        (100, -30, "Сумма должна быть больше нуля")
    ],
)
def test_make_transfer_errors(balance, amount, message_error):
    with pytest.raises(ValueError, match=message_error):
        make_transfer(balance, amount)

@pytest.mark.parametrize(
    "balance, amount",
    [
        (100, float("nan")),
        (100, float("inf")),
        (100, float("-inf"))
    ],
)
def test_can_transfer(balance, amount):
    with pytest.raises(ValueError):
        make_transfer(balance, amount)

@pytest.mark.parametrize(
    "balance, amount, result",
    [
        (1000, 300, 700),
        (500, 500, 0)
     ],
)
def test_make_transfer_success(balance, amount, result):
    assert make_transfer(balance, amount) == result

from file_practice import find_account

@pytest.mark.parametrize(
    "lst, key, amount, result",
    [([
    {
        "account_number": "101",
        "balance": 4000
    },
    {
        "account_number": "102",
        "balance": 2500
    },
    {
        "account_number": "103",
        "balance": 7000
    }
], "102", 500, (True, 3000)),
        (
[
    {
        "account_number": "101",
        "balance": 4000
    },
    {
        "account_number": "102"
    },
    {
        "account_number": "103",
        "balance": 7000
    }
],"102", 500, (False, None)),
        (
[
    {
        "account_number": "101",
        "balance": 4000
    },
    {
        "account_number": "103",
        "balance": 7000
    }
],"102", 500, (False, None))
    ],

)
def test_find_account_success(lst, key, amount, result):
    assert find_account(lst, key, amount) == result
    if result[0]:
        for i in lst:
            if i["account_number"] == key:
                assert i["balance"] == result[1]