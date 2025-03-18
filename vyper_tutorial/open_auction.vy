# pragma version >0.3.10

# Open Auction Contract

# Auction params
# Beneficiary recieves money from the highest bidder
beneficiary: public(address)
auction_start: public(uint256)
auction_end: public(uint256)

# Current state of the auction
highest_bidder: public(address)
highest_bid: public(uint256)

# Set to true at the end, disallows any change
ended: public(bool)

# Keep track of refunded bids so we can follow the withdraw pattern
pending_returns: public(HashMap[address, uint256])

# Create a simple auction with '_auction_start' and 
# '_bidding_time' seconds bidding on behalf of the 
# beneficiary address '_beneficiary'. 
@deploy
def __init__(_beneficiary: address, _auction_start: uint256, _bidding_time: uint256):
    self.beneficiary = _beneficiary
    self.auction_start = _auction_start
    self.auction_end = _auction_start + _bidding_time
assert block.timestamp < self.auction_end

# Bid on the auction with the value sent 
# together with this transaction.
# The value will only be refunded if the 
# auction is not won.
@external
@payable
def bid():
    # Check if bidding period has started
    assert block.timestamp >= self.auction_start
    # Check if bidding period is over
    assert block.timestamp < self.auction_end
    # Check if the bid is high enough
    assert msg.value > self.highest_bid
    # Track the refund for the previous highest bidder
    self.pending_returns[self.highest_bidder] += self.highest_bid  
    # Track new high bid
    self.highest_bidder = msg.sender
    self.highest_bid = msg.value

# Withdraw a bid that was overbid.The withdraw pattern is 
# used here to avoid a security issue. If refunds were directly
# sent as part of the bid() function, a malicious bidder could block
# those refunds and thus block new higher bids from coming in.
@external
def withdraw():
    pending_amount: uint256 = self.pending_returns[msg.sender]
    self.pending_returns[msg.sender] = 0
        send(msg.sender, pending_amount)
    
# End the auction and send the highest bid 
# to the beneficiary
@external
def end_auction():
    # it is a good guideline to structure functions that interact
    # with other contracts(ie, they call functions or send Ether)
    # into three phases:
    # 1. checking conditions
    # 2. performing actions (potentially changing conditions)
    # 3. interacting with other contracts
    # If these phases are mixed up, the other contract could call
    # back into the current contract and modify the state or cause
    # effects (ether payout) to be performed multiple times.
    # If functions called internally include interaction with external
    # contracts, they also have to be considered interaction with external
    # contracts.

    # 1. Conditions
    # Check if auctin end time has been reached
    assert block.timestamp >= self.auction_end
    # Check if this function has already been called
    assert not self.ended

    # 2. Effects
    self.ended = True

    # 3. Interaction
    send(self.beneficiary, self.highest_bid)
    

