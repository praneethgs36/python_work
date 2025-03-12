from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print(f"Python script is connected?")

account_balance = w3.eth.get_balance('0x7f2164C3313e94aEC49C04Fb50996994a768BB44')
print(f"The balance of the 3rd account is {account_balance}")