from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

sender_private_key = "0x869e6487bc1c435731bbf8bf97aca8b9f0cff4ccbe30f4f830d26fbc3d382555"
sender_address = "0x7f2164C3313e94aEC49C04Fb50996994a768BB44"

recipient_address = "0xdEC3285F5eB1245a5f6cF7825c0ABa0c7769050a"

amount = Web3.to_wei(5, 'ether')

transaction = {
    'from': sender_address,
    'to': recipient_address,
    'value': amount,
    'gas': 21000,
    'gasPrice': Web3.to_wei(10, 'gwei'),
    'nonce': w3.eth.get_transaction_count(sender_address),  
}

signed_transaction = w3.eth.account.sign_transaction(transaction, sender_private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash.hex())
