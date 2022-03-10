from brownie import (
    GuessTheSecretNumberChallenge,
    config,
    accounts,
    convert,
    SecretAttack,
    GuessTheRandomNumberChallenge,
    GuessTheNewNumberChallenge,
    RandomAttack,
)
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))


amount = Web3.toWei(1, "ether")
# make n = keccak245(blockhas.....) in another solidity
# contract that calls the 'guess' func to pass it as argument

# pass n to guess


def test_newnumber():
    account = get_account()
    new_number = GuessTheNewNumberChallenge.deploy({"from": account, "value": amount})
    attacker = RandomAttack.deploy({"from": account, "value": amount})
    attacker.attack(new_number.address)
    assert new_number.isComplete == True
