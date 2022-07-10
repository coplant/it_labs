class Node:
    def __init__(self, value, frequency, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
        self.code = ""


def get_frequency(data):
    """
    Calculating data's frequency
    :param data: Input string
    :return: Dictionary of chars' number
    """
    frequency = dict()
    for item in data:
        if not frequency.get(item):
            frequency[item] = 1
        else:
            frequency[item] += 1
    return frequency


def get_code(root, codes=dict(), code=''):
    """
    Calculating Huffman's alphabet (codes)
    :param root: Current handling node
    :param codes: Huffman's alphabet - Dictionary {char: code}
    :param code: Current char code
    :return: Codes
    """
    if root is None:
        return
    current_code = code + root.code
    get_code(root.left, codes, code=current_code)
    get_code(root.right, codes, code=current_code)
    if not root.left and not root.right:
        codes[root.value] = current_code
    return codes


def coding(data):
    """
    Huffman coding handler
    :param data: Input string
    :return: Codes (Alphabet)
    """
    frequency = get_frequency(data)
    tree = [Node(item, frequency.get(item)) for item in frequency]
    while len(tree) != 1:
        sorted(tree, key=lambda item: item.frequency)
        left = tree[0]
        left.code = '0'
        right = tree[1]
        right.code = '1'
        freq = left.frequency + right.frequency
        tree.remove(left)
        tree.remove(right)
        tree.append(Node("", freq, left, right))
    return get_code(tree[0])


def encode(string, alpha):
    """
    Encoding string using Huffman's code
    :param string: Input string
    :param alpha: Codes (Alphabet)
    :return: Encoded string
    """
    encoded = ''
    for char in string:
        encoded += alpha[char]
    return encoded


def decode(string, alpha):
    """
    Decoding string using Huffman's code
    :param string: Input string
    :param alpha: Codes (Alphabet)
    :return: Decoded string
    """
    decoded = ""
    while string:
        for key, value in alpha.items():
            if string.startswith(value):
                decoded += key
                string = string[len(value):]
    return decoded


def main():
    string = input("Enter data: ")
    alpha = coding(string)
    encoded_string = encode(string, alpha)
    decoded_string = decode(encoded_string, alpha)
    print(f"Alphabet:")
    for key, value in alpha.items():
        print(f'\t\t{key} - {value}')
    print(f"Encoded string: {encoded_string}\nDecoded string: {decoded_string}")


if __name__ == '__main__':
    main()
