from brownie import (
    PredictTheFutureChallenge,
    FutureAttack,
    chain,
)
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth
import time

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))


amount = Web3.toWei(1, "ether")


def test_future():
    account = get_account()
    future = PredictTheFutureChallenge.deploy({"from": account, "value": amount})
    attacker = FutureAttack.deploy(future.address, {"from": account, "value": amount})
    tx = attacker.lockIn({"from": account})

    chain.mine(100)
    while future.isComplete() == False:

        attacker.attack({"from": account})
    assert future.isComplete() == True
