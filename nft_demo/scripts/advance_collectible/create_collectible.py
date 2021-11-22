from brownie import AdvanceCollectible
from scripts.helpful import fund_with_link, get_account
from web3 import Web3


def main():
    account = get_account()
    advanced_collectible = AdvanceCollectible[-1]
    fund_with_link(advanced_collectible.address,
                   amount=Web3.toWei(0.1, "ether"))

    # Create collectible
    creating_tx = advanced_collectible.createCollectible(
        {"from": account})
    creating_tx.wait(1)
    print("New token has been created!!!")
