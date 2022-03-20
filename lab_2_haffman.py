from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes
    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')
    return codes


def get_tree(string):
    prob = {}
    string_count = Counter(string)
    for k, v in string_count.items():
        prob[k] = round((v / len(string)), 5)
    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}
    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]
    return [key for key in string_count][0], prob


def coding(string, alpha):
    encoded_string = ''
    for char in string:
        encoded_string += alpha[char]
    return encoded_string


def encode(string):
    tree, prob = get_tree(string)
    alpha = get_code(tree)
    coding_str = coding(string, alpha)
    print(f'Probability: {prob}')
    print(f'Alphabet: {alpha}')
    print(f'Encoding Result: {coding_str}')


def main():
    string = input('Enter string: ')
    encode(string)


if __name__ == '__main__':
    main()