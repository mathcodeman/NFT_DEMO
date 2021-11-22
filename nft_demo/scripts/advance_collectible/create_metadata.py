from brownie import AdvanceCollectible, network
from scripts.helpful import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path


def main():
    advance_collectible = AdvanceCollectible[-2]
    number_of_advanced_collectible = advance_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectible} collectibles")

    for token_id in range(number_of_advanced_collectible):
        breed = get_breed(advance_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        print(metadata_file_name)
    collectible_metadata = metadata_template
    if Path(metadata_file_name).exists():
        print(f"{metadata_file_name} already exsits! Delete")
    else:
        print(f"Creating Metadata file: {metadata_file_name}")
        collectible_metadata["name"] = breed
        collectible_metadata["description"] = f"An cute {breed}!!!"
        print(collectible_metadata)
        image_path = "./pic/" + breed.lower().replace("_", "-") + ".png"
        print(image_path)
        #image_uri = upload_to_ipfs()
        #collectible_metadata["image_uri"] = image_uri


def uoload_to_ipfs(file_path):
    with Path(file_path).open("rb") as fp:
        image_binary = fp.read()
