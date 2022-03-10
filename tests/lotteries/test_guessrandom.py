from brownie import (
    GuessTheSecretNumberChallenge,
    config,
    accounts,
    convert,
    SecretAttack,
    GuessTheRandomNumberChallenge,
)
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))


amount = Web3.toWei(1, "ether")


def test_guessrandom():
    account = get_account()
    guess_random = GuessTheRandomNumberChallenge.deploy(
        {"from": account, "value": amount}
    )

    n = web3.eth.get_storage_at(guess_random.address, 0)
    # call guess function
    guess_random.guess(n, {"from": account, "value": amount})
    # assert isComplete
    assert guess_random.isComplete() == True
