import os
from mnemonic import Mnemonic
from web3 import Web3
w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

riches_file = "./riches.txt"

with open(riches_file, "r") as file:
    riches = file.read().splitlines()

i = 0
while True:
    mnemonic = Mnemonic("english").generate(128)
    #mnemonic = "picnic piece leader setup flame crouch cradle helmet trophy intact solar number"
    acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}")
    address = acc.address

    print(f" {address}")

    if address in riches:
        print("\a")
        print("\033[32m>> Success:", address, "\033[0m")
        private_key = Web3.to_hex(acc.key)
        success_string = f"Wallet: {address}\n\nPrivate Key: {private_key}\n\n12 word phrase: {mnemonic}"

        with open("./Success.txt", "w") as success_file:
            success_file.write(success_string)
        
        os._exit(0)

    i += 1
