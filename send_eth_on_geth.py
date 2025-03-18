from web3 import Web3

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))
with open("my_keystore/UTC--2025-03-16T16-06-23.105182629Z--bbd932c75187f7fe1cbe8fd43fcddbc5e79b93de") as keyfile:
    encrypted_key = keyfile.read()
    password = 'lightningnetwork'
    sender_private_key = w3.eth.account.decrypt(encrypted_key, password)
sender_address = "0x9c40b8e196f9dc48566eb2222c9db08aaf154249"
recipient_address = Web3.to_checksum_address("bbd932c75187f7fe1cbe8fd43fcddbc5e79b93de")
amount = w3.to_wei(2, 'ether')

transaction = {
    "chainId": 1337,
    "from": sender_address,
    "to": recipient_address,
    "value": amount,
    "gas": 21000,
    "gasPrice": Web3.to_wei('50', 'gwei'),
    "nonce": w3.eth.get_transaction_count(sender_address),
}

signed_transaction = w3.eth.account.sign_transaction(transaction, sender_private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print(f"Transaction hash: {transaction_hash.hex()}")