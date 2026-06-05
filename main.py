from src.huffman import HuffmanCoding


def main():

    print("\n====================================")
    print(" Dynamic File Compression Utility ")
    print("====================================\n")

    file_path = input(
        "Enter path of text file: "
    )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

    except FileNotFoundError:

        print("\nFile not found.")
        return

    huffman = HuffmanCoding()

    compressed_text, codes = (
        huffman.compress(text)
    )

    decompressed_text = (
        huffman.decompress(
            compressed_text
        )
    )

    original_bits = (
        len(text) * 8
    )

    compressed_bits = (
        len(compressed_text)
    )

    saved = (
        (
            original_bits
            - compressed_bits
        )
        / original_bits
    ) * 100

    print("\n========== HUFFMAN CODES ==========\n")

    for char, code in codes.items():

        if char == "\n":
            display_char = "\\n"

        elif char == " ":
            display_char = "' '"

        else:
            display_char = char

        print(
            f"{display_char} -> {code}"
        )

    print(
        "\n========== COMPRESSION REPORT ==========\n"
    )

    print(
        f"Original Size   : {original_bits} bits"
    )

    print(
        f"Compressed Size : {compressed_bits} bits"
    )

    print(
        f"Space Saved     : {saved:.2f}%"
    )

    print(
        "\n========== VERIFICATION ==========\n"
    )

    if text == decompressed_text:

        print(
            "SUCCESS: Decompressed text matches original."
        )

    else:

        print(
            "ERROR: Verification failed."
        )

    save_choice = input(
        "\nSave compressed output? (y/n): "
    )

    if save_choice.lower() == "y":

        with open(
            "compressed.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                compressed_text
            )

        print(
            "Compressed file saved as compressed.txt"
        )

    save_choice = input(
        "\nSave decompressed output? (y/n): "
    )

    if save_choice.lower() == "y":

        with open(
            "decompressed.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                decompressed_text
            )

        print(
            "Decompressed file saved as decompressed.txt"
        )


if __name__ == "__main__":
    main()