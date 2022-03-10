from brownie import GuessTheNumberChallenge, config, accounts, convert
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3

amount = Web3.toWei(2, "ether")


def test_guessthenumber():
    account = get_account()
    guess_number = GuessTheNumberChallenge.deploy({"from": account})
    guess_number.guess(42, {"from": account, "value": amount})
    assert guess_number.isComplete() == True
