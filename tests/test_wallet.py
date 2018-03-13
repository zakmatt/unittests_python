import pytest
from ..wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """return wallet instance with balance equal 0"""
    return Wallet()


@pytest.fixture
def wallet():
    """return wallet instance with balance of 30"""
    return Wallet(30)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 30


def test_wallet_add_cash(wallet):
    wallet.add_cash(40)
    assert wallet.balance == 70


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 20


def test_wallet_spend_cash_raises_insufficient_amount(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(50)


@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
