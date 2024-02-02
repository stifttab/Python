import pytest
from unittest.mock import patch
from io import StringIO
from project import withdraw, deposit

def test_withdraw_sufficient_balance():
    account = {'balance': 100.0}
    withdraw(account, 50.0)
    assert account['balance'] == 50.0

def test_withdraw_insufficient_balance():
    account = {'balance': 30.0}
    with pytest.raises(ValueError, match="Insufficient funds!"):
        withdraw(account, 50.0)

def test_withdraw_invalid_amount():
    account = {'balance': 100.0}
    with pytest.raises(ValueError, match="Invalid withdrawal amount."):
        withdraw(account, -50.0)

def test_deposit_valid_amount():
    account = {'balance': 100.0}
    deposit(account, 50.0)
    assert account['balance'] == 150.0

def test_deposit_invalid_amount():
    account = {'balance': 100.0}
    with pytest.raises(ValueError, match="Invalid deposit amount."):
        deposit(account, -50.0)

def test_save_accounts_after_withdraw():
    accounts = {'123': {'account_number': '123', 'balance': 100.0}}
    withdraw(accounts['123'], 50.0)
    assert accounts['123']['balance'] == 50.0

def test_save_accounts_after_deposit():
    accounts = {'123': {'account_number': '123', 'balance': 100.0}}
    deposit(accounts['123'], 50.0)
    assert accounts['123']['balance'] == 150.0
