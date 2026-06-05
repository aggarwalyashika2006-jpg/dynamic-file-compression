import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:

    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}

    def calculate_frequency(self, text):
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        return freq

    def build_heap(self, freq):
        heap = []
        for ch, fr in freq.items():
            heapq.heappush(heap, Node(ch, fr))
        return heap

    def build_tree(self, heap):
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]

    def generate_codes(self, node, current=""):
        if not node:
            return

        if node.char is not None:
            self.codes[node.char] = current
            self.reverse_codes[current] = node.char
            return

        self.generate_codes(node.left, current + "0")
        self.generate_codes(node.right, current + "1")

    def compress(self, text):
        freq = self.calculate_frequency(text)
        heap = self.build_heap(freq)
        root = self.build_tree(heap)

        self.codes = {}
        self.reverse_codes = {}
        self.generate_codes(root)

        compressed = "".join(self.codes[c] for c in text)
        return compressed, self.codes

    def decompress(self, compressed):
        current = ""
        result = ""

        for bit in compressed:
            current += bit
            if current in self.reverse_codes:
                result += self.reverse_codes[current]
                current = ""

        return result