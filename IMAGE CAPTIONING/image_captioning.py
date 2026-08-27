"""
CODSOFT AI Internship - Task 3
Image Captioning

This project demonstrates an image-captioning pipeline using a
pre-trained image recognition model (ResNet50) for feature extraction
and a pretrained image-to-text model (BLIP) for caption generation.

Run:
    pip install -r requirements.txt
    python image_captioning.py path/to/image.jpg

The first run downloads the required pretrained models.
"""

import argparse
from pathlib import Path

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


def generate_caption(image_path: str) -> str:
    """Generate a natural-language caption for an input image."""
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    image = Image.open(path).convert("RGB")

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption


def main():
    parser = argparse.ArgumentParser(
        description="Generate a caption for an image using a pretrained BLIP model."
    )
    parser.add_argument(
        "image",
        help="Path to the image file (JPG, JPEG, PNG, etc.)"
    )
    args = parser.parse_args()

    try:
        caption = generate_caption(args.image)
        print("\nGenerated Caption:")
        print(caption)
    except Exception as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()
