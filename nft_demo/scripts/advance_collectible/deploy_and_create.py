from scripts.helpful import get_account, OPENSEA_URL, get_contract, config, fund_with_link
from brownie import AdvanceCollectible, network
from web3 import Web3


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvanceCollectible.deploy(get_contract("vrf_coordinator"), get_contract(
        "link_token"), config["networks"][network.show_active()]["KEY_HASH"], config["networks"][network.show_active()]["fee"], {"from": account}, publish_source=config["networks"][network.show_active()].get("verify", False))
    fund_with_link(advanced_collectible.address,
                   amount=Web3.toWei(0.1, "ether"))

    # Create collectible
    creating_tx = advanced_collectible.createCollectible(
        {"from": account})
    print(type(creating_tx))
    creating_tx.wait(1)
    print("New token has been created!!!")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
