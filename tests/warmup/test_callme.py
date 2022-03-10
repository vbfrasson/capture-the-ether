from brownie import CallMeChallenge, config, accounts
from scripts.helpful_scripts import *


def test_callme():
    account = get_account()
    call_me = CallMeChallenge.deploy({"from": account})
    call_me.callme()
    assert call_me.isComplete() == True
