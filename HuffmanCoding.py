import heapq

def huffman_coding():
    text = input("Enter a string: ")
    if not text:
        return

    # 1. Calculate frequencies
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # 2. Build Min-Heap
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)

    # 3. Build Huffman Tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # 4. Generate Codes
    huff_dict = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    codes = {c: code for c, code in huff_dict}

    # 5. Encoding
    encoded_str = "".join(codes[char] for char in text)

    # 6. Decoding
    decoded_str = ""
    temp_code = ""
    reverse_codes = {v: k for k, v in codes.items()}
    for bit in encoded_str:
        temp_code += bit
        if temp_code in reverse_codes:
            decoded_str += reverse_codes[temp_code]
            temp_code = ""

    # Output Results
    print("\nCharacter Frequencies:", freq)
    print("Huffman Codes:", codes)
    print("Encoded String:", encoded_str)
    print("Decoded String:", decoded_str)

if __name__ == "__main__":
    huffman_coding()