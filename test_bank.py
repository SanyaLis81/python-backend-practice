from fileinput import filename

import bank


def test_successful_transfer():
    assert bank.transfer(1000, 500, 300) == (700, 800, True)


def test_insufficient_funds():
    assert bank.transfer(100, 500, 200) == (100, 500, False)


def test_zero_transfer():
    assert bank.transfer(1000, 500, 0) == (1000, 500, False)


def test_string_amount():
    assert bank.transfer(1000, 500, "100") == (1000, 500, False)


def test_nan_amount():
    assert bank.transfer(1000, 500, float("nan")) == (1000, 500, False)


def test_negative_balance_tr():
    assert bank.transfer(-1000, 500, 100) == (-1000, 500, False)


def test_transfer_entire_balance():
    balance_from, balance_to, success = bank.transfer(1000, 500, 1000)
    assert balance_from == 0
    assert balance_to == 1500
    assert success is True

def test_get_account_info():
    assert bank.get_account_info(1250) == "Баланс счёта: 1250.00"

def test_get_account_info_negative():
    assert bank.get_account_info(-10) is None

def test_get_account_info_str():
    assert bank.get_account_info("100") is None

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

from file_practice import find_account, deposit_to_account, load_accounts, get_account_info, get_account_info_from_file, withdraw_from_account

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
    old_balance =None
    for account in lst:
        if account["account_number"] == key and "balance" in account:
            old_balance = account["balance"]
            break
    assert find_account(lst, key, amount) == result
    if result[0]:
        for i in lst:
            if i["account_number"] == key:
                assert i["balance"] == result[1]
    else:
        if old_balance != None:
            for account in lst:
                if account["account_number"] == key and "balance" in account:
                    assert old_balance == account["balance"]
        else:
            for account in lst:
                if account["account_number"] == key and "balance" in account:
                    assert old_balance == account["balance"]
                elif account["account_number"] == key and "balance" not in account:
                    assert "balance" not in account

import json

def test_deposit_to_account(tmp_path):
    filename = tmp_path / "account.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([
            {"account_number": "102", "balance": 2500}
        ], file)
    assert deposit_to_account(filename, "102", 500) is True
    with open(filename, "r", encoding="utf-8") as file:
        new_data = json.load(file)
    for account in new_data:
        if account["account_number"] == "102" and "balance" in account:
            assert account["balance"] == 3000

def test_deposit_to_account_not_found(tmp_path):
    filename = tmp_path / "account.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([
            {"account_number": "102", "balance": 2500}
        ], file)
    assert deposit_to_account(filename, "999", 500) is False
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    for account in data:
        if account["account_number"] == "102" and "balance" in account:
            assert account["balance"] == 2500

def test_not_balance_deposit_to_account(tmp_path):
    filename = tmp_path / "tm_file.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([{"account_number": "102"}], file)
    assert deposit_to_account(filename, "102", 500) is False
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    for account in data:
        if account["account_number"] == "102":
            assert "balance" not in account
def test_deposit_invalid_json(tmp_path):
    filename = tmp_path / "broken.json"

    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "balance": 2500}')
    with pytest.raises(ValueError, match="Файл содержит некорректный JSON"):
        deposit_to_account(filename, "102", 500)
def test_deposit_not_file(tmp_path):
    filename = tmp_path / "missing.json"

    with pytest.raises(ValueError, match="Файл не найден"):
        deposit_to_account(filename, "102", 500)
    assert filename.exists() is False

def test_load_accounts_invalid_type(tmp_path):
    filename = tmp_path / "string.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('"привет"')
    with pytest.raises(ValueError, match="Файл должен содержать список счетов"):
        load_accounts(filename)

def test_load_accounts_invalid_item(tmp_path):
    filename = tmp_path / "withoutdict.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('["привет", 123]')
    with pytest.raises(ValueError, match="Каждый счёт должен быть словарём"):
        load_accounts(filename)

def test_load_accounts_empty_list(tmp_path):
    filename = tmp_path / "empty.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[]')
    with pytest.raises(ValueError, match="Список счетов пуст"):
        load_accounts(filename)

def test_get_account_info_found(tmp_path):
    filename = tmp_path / "get_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    with open(filename, "r", encoding="utf-8") as file:
        info = json.load(file)
    assert get_account_info(info, "102") == {"account_number": "102", "owner": "Александр", "balance": 3000}

def test_get_account_info_not_found(tmp_path):
    filename = tmp_path / "not_found.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    with open(filename, "r", encoding="utf-8") as file:
        info = json.load(file)
    assert get_account_info(info, "999") is None

def test_get_account_info_from_file(tmp_path):
    filename = tmp_path / "get_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    assert get_account_info_from_file(filename, "102") == {"account_number": "102", "owner": "Александр", "balance": 3000}

def test_get_account_info_from_file_not_found(tmp_path):
    filename = tmp_path / "get_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    assert get_account_info_from_file(filename, "999") is None

def test_withdraw_from_account_success(tmp_path):
    filename =tmp_path / "withdraw_from_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    assert withdraw_from_account(filename, "102", 500) is True
    assert get_account_info_from_file(filename, "102")["balance"] == 2500

def test_withdraw_from_account_insufficient_funds(tmp_path):
    filename = tmp_path / "withdraw_from_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    assert withdraw_from_account(filename, "102", 3500) is False
    assert get_account_info_from_file(filename, "102")["balance"] == 3000

def test_withdraw_from_account_not_found(tmp_path):
    filename = tmp_path / "withdraw_from_account.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write('[{"account_number": "102", "owner": "Александр", "balance": 3000}]')
    assert withdraw_from_account(filename, "999", 500) is False
    assert get_account_info_from_file(filename, "102")["balance"] == 3000