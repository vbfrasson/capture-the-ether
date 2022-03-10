from brownie import (
    GuessTheSecretNumberChallenge,
    config,
    accounts,
    convert,
    SecretAttack,
)
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3


"""
Keccak algorithm implement in solidity. 
Look for the solution in contracts/SecretAttack.sol
"""

amount = Web3.toWei(1, "ether")


def test_secretnumber():
    account = get_account()
    secret_attack = SecretAttack.deploy({"from": account})
    secret = GuessTheSecretNumberChallenge.deploy({"from": account})

    secret_attack.attack()

    n = secret_attack.i()

    secret.guess(n, {"from": account, "value": amount})
    assert secret.isComplete() == True
