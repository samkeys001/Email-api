import random
import time
from web3 import Web3
from eth_account import Account

Account.enable_unaudited_hdwallet_features()
infura_url = "https://eth-mainnet.public.blastapi.io"  # "https://mainnet.infura.io/v3/9a3906307b31463d84305baf3daf329b"
infura_url_poly = "https://polygon-mainnet.public.blastapi.io"  # "https://polygon-mainnet.infura.io/v3/9a3906307b31463d84305baf3daf329b"
web3 = Web3(Web3.HTTPProvider(infura_url))
web3_poly = Web3(Web3.HTTPProvider(infura_url_poly))
import random

# Your list of strings

updated_line = []
shuffles_seed = updated_line


file = open('word.txt', 'r')
lines = file.readlines()
for line in lines:
    new_line = line.strip().split()
    for line_1 in new_line:
        updated_line.append(line_1)

while True:
 try:
    shuffled_list = random.sample(shuffles_seed, len(shuffles_seed))
    word_list = random.sample(shuffled_list, 12)
    phrase = ' '.join(word_list)
     # Your Ethereum mnemonic phrase
    mnemonic_phrase = phrase
    account = Account.from_mnemonic(mnemonic_phrase)
    private_key = account.key.hex()
    if private_key:
        print(f'seed_phrase: {mnemonic_phrase}')
        time.sleep(0.5)
        file = open('extracted_seed.txt', 'a')
        file.write(mnemonic_phrase + '\n')
        web3.eth.account = account
        if web3.is_connected():
            print(f"Account Address: {account.address}")
            balance_wei = web3.eth.get_balance(account.address)
            balance_eth = web3.from_wei(balance_wei, 'ether')
            file = open('seed_balance.txt', 'a')
            file.write(f' {mnemonic_phrase}  value:{balance_eth} eth\n')
            file.close()
            print(f'Value:{balance_eth} ETH')
            if balance_eth > 0:
                file = open('eth_balance_main.txt', 'a')
                file.write(f' {mnemonic_phrase}  value:{balance_eth}  eth\n')
        if web3_poly.is_connected():
            # print(f"Account Address: {account.address}")
            balance_wei = web3_poly.eth.get_balance(account.address)
            balance_eth_poly = web3_poly.from_wei(balance_wei, 'ether')
            file = open('seed_balance_poly.txt', 'a')
            file.write(f' {mnemonic_phrase}  value:{balance_eth_poly} ETH in polygon\n')
            file.close()
            print(f'Value:{balance_eth_poly} ETH in polygon')
            if balance_eth_poly > 0:
                file = open('polybalance_main.txt', 'a')
                file.write(f' {mnemonic_phrase}  value:{balance_eth_poly}  polygon\n')
                file.close()




        else:
            print("Connection failed.")
            time.sleep(0.1)



 except:
    print(f'invalid seed phrase: {mnemonic_phrase}')
    time.sleep(0.1)
