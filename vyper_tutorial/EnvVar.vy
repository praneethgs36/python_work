# @version ^0.3.10

donatur: address
donation: uint256
time: uint256


@payable
@external
def donate():
    self.donatur = msg.sender
    self.donation = msg.value
    self.time = block.timestamp
    