
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
