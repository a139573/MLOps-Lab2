import random
from PIL import Image
from io import BytesIO

# The 37 actual classes from the Oxford-IIIT Pet Dataset
OXFORD_PET_CLASSES = [
    "Abyssinian", "American_Bulldog", "American_Pit_Bull_Terrier", "Basset_Hound",
    "Beagle", "Bengal", "Birman", "Bombay", "Boxer", "British_Shorthair",
    "Chihuahua", "Egyptian_Mau", "English_Cocker_Spaniel", "English_Setter",
    "German_Shorthaired", "Great_Pyrenees", "Havanese", "Japanese_Chin",
    "Keeshond", "Leonberger", "Maine_Coon", "Miniature_Pinscher", "Newfoundland",
    "Persian", "Pomeranian", "Pug", "Ragdoll", "Russian_Blue", "Saint_Bernard",
    "Samoyed", "Scottish_Terrier", "Shiba_Inu", "Siamese", "Sphynx",
    "Staffordshire_Bull_Terrier", "Wheaten_Terrier", "Yorkshire_Terrier"
]

def predict_img_class(img):
    """
    Randomly predicts a class from the Oxford-IIIT Pet Dataset.
    """
    # Simply pick one random breed from the list
    return random.choice(OXFORD_PET_CLASSES)

def resize_image(image_bytes: bytes, width: int, height: int) -> bytes:
    """
    Resize an input image to the given width and height.
    Returns the resized image as bytes (JPEG format).
    """
    with Image.open(BytesIO(image_bytes)) as img:
        # Convert to RGB to ensure compatibility (e.g. if input is PNG with transparency)
        img = img.convert("RGB")
        resized = img.resize((width, height))
        output = BytesIO()
        resized.save(output, format="JPEG")
        return output.getvalue()