from src.huffman import HuffmanCoding

from src.file_handler import (
    read_file,
    save_file
)

from src.statistics import (
    compression_report
)


def main():

    print(
        "\n===== Dynamic File Compression Utility =====\n"
    )

    input_path = (
        "input_files/sample.txt"
    )

    text = read_file(
        input_path
    )

    print(
        "Original Text:\n"
    )

    print(text)

    huffman = HuffmanCoding()

    (
        compressed_text,
        codes
    ) = huffman.compress(
        text
    )

    save_file(
        "compressed_files/compressed.txt",
        compressed_text
    )

    decompressed_text = (
        huffman.decompress(
            compressed_text
        )
    )

    save_file(
        "decompressed_files/decompressed.txt",
        decompressed_text
    )

    print(
        "\n===== Huffman Codes =====\n"
    )

    for char, code in codes.items():

        print(
            repr(char),
            "=>",
            code
        )

    report = (
        compression_report(
            text,
            compressed_text
        )
    )

    print(
        "\n===== Report =====\n"
    )

    print(
        "Original Size:",
        report["original_bits"],
        "bits"
    )

    print(
        "Compressed Size:",
        report["compressed_bits"],
        "bits"
    )

    print(
        "Compression Ratio:",
        report["ratio"],
        "%"
    )

    print(
        "Space Saved:",
        report["saved"],
        "%"
    )

    print(
        "\n===== Verification =====\n"
    )

    if text == decompressed_text:

        print(
            "SUCCESS"
        )

    else:

        print(
            "FAILED"
        )


if __name__ == "__main__":

    main()