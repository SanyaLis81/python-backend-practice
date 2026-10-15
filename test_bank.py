
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


def test_negative_balance():
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
