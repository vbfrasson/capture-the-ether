pragma solidity ^0.4.21;

contract SecretAttack {
    bytes32 answerHash =
        0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365;

    uint8 public i = 0;

    function attack() public returns (uint8) {
        for (i = 0; i < 255; i++) {
            if (keccak256(i) == answerHash) {
                return i;
            }
        }
    }
}
