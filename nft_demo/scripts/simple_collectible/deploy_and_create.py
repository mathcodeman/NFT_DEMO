from scripts.helpful import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_tokenURI = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(
        sample_tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"NFT deployed!!! on {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter() - 1)}")
    return simple_collectible


def main():
    deploy_and_create()
