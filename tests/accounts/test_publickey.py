"""
When an account sends a transaction the serial transaction hash gets signed
with ECDSA. ECDSA consists of (r,s,v) which can be used to recover the
public key of the sender account.
--- Find out how to get (r,s,v) and recover public key from them using Web3.py
"""

# send a transaction from the contract to be hacked
#  get transaction hex
