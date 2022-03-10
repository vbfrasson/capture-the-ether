from brownie import CaptureTheEther, config, accounts, convert
from eth_utils import to_bytes
from scripts.helpful_scripts import *
from web3 import Web3

# Ropsten contract address: 0xc3D2cb7D8d6f203eD6021e0E81E8ae8FCfD2323D
def test_nickname():
    account = get_account()
    nickname = CaptureTheEther.deploy({"from": account})
    nickname.setNickname(Web3.toBytes(text="Vitor"))
    # print(nickname.nicknameOf[account]())
    assert nickname.nicknameOf(account) == Web3.toHex(text="Vitor")
