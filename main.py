import hashlib
import numpy as np
import cv2


def get_sha384_hash(number):
    number_str = str(number).encode('utf-8')
    sha384_hash = hashlib.sha384(number_str).hexdigest()
    return sha384_hash


def split_hash(hash_str, parts=16):
    part_length = len(hash_str) // parts
    return [hash_str[i * part_length:(i + 1) * part_length] for i in range(parts)]


def hex_to_rgb(hex_str):
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return r, g, b


def create_image(rgb_list, size=(4, 4)):
    img_array = np.array(rgb_list, dtype=np.uint8)
    img_array = img_array.reshape((size[0], size[1], 3))
    return img_array


def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    hash_str = get_sha384_hash(number)
    print(f"SHA384 Hash: {hash_str}")

    hash_parts = split_hash(hash_str, parts=16)
    print(f"Hash divided into 16 parts: {hash_parts}")

    rgb_colors = [hex_to_rgb(part) for part in hash_parts]
    print(f"RGB Color Codes: {rgb_colors}")

    image = create_image(rgb_colors, size=(4, 4))

    scale_factor = 250  # Scale factor to enlarge the image
    scaled_image = cv2.resize(
        image,
        (image.shape[1] * scale_factor, image.shape[0] * scale_factor),
        interpolation=cv2.INTER_NEAREST
    )

    output_filename = "output_image.png"
    cv2.imwrite(output_filename, scaled_image)
    print(f"Image saved as '{output_filename}'.")
    cv2.imshow("4x4 Image", scaled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
