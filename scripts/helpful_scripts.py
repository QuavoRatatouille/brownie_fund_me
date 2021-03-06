from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCHCHAIN_ENVIRONEMNTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCHCHAIN_ENVIRONEMNTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks Deployed!")
