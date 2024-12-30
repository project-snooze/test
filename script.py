pictures=[
    "https://assets.objkt.media/file/assets-003/QmZf8wPUf3jKwGpvYWVZUdFwQwcqKGcBzBwAAvkzEbsnLL/artifact",
    "https://assets.objkt.media/file/assets-003/QmVm1VGQqSpHfxg7rwTtGePvy2wk8oCLHuoJSLqtbJwgda/artifact",
    "https://assets.objkt.media/file/assets-003/QmcxUANf98ZJ8pkA5Hw27xJ4psQzJgfkPfwkoezpmYp5eD/artifact",
    "https://assets.objkt.media/file/assets-003/QmUM89fPVurk4dcSruEphN9Vq9aWWXpMHN2DDon5UYJ9YK/artifact",
    "https://assets.objkt.media/file/assets-003/QmYnTJmmSvoB76KooTwkM8pYT2BseRJXSeS1AK2XGpcMuB/artifact",
    "https://assets.objkt.media/file/assets-003/QmSCGzzsWDuwirttHmRK4KZTxfHFLDDnogcJ1YR3S9KGSk/artifact",
    "https://assets.objkt.media/file/assets-003/QmVTbnjdVyDt1RSTvn3frb7nUXzDd4ygnvMu538qBsYgE9/artifact",
]

import os
import json

# Directory to save the metadata files
output_dir = "metadata"

# Function to generate metadata
def generate_metadata(pictures):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, picture in enumerate(pictures):
        metadata = {
            "name": f"NFT #{index + 1}",  # Generate a unique name
            "description": "This is a randomly generated NFT description.",  # Fixed description
            "image": picture,  # Use the image link from the array
            "attributes": [
                {"trait_type": "rarity", "value": "common"},  # Example fixed trait
                {"trait_type": "generation", "value": 1},  # Example fixed trait
            ],
        }

        # File name for the metadata JSON
        file_name = f"{index + 1}.json"
        file_path = os.path.join(output_dir, file_name)

        # Write JSON to file
        with open(file_path, "w") as f:
            json.dump(metadata, f, indent=2)

        print(f"Generated: {file_name}")

# Generate metadata files
generate_metadata(pictures)
