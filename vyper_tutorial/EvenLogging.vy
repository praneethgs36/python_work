# @version 0.3.0

event Donation:
    donatur : indexed(address):
    amount: uint256


@payable
@external
def donate():
    log Donation(msg.sender, msg.value)
    
