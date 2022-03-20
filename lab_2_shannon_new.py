from collections import Counter

TERNARY = 3


class Node:
    def __init__(self, value, left=None, mid=None, right=None):
        self.right = right
        self.mid = mid
        self.left = left
        self.value = value

    def __len__(self):
        if self.value:
            return len(self.value)
        else:
            return 0


def get_indexes(spam, precision):
    div_spam = []
    intervals = []
    total = 0

    for i in range(len(spam) - 1):
        if abs(spam[i][1] - precision) < abs(spam[i][1] + spam[i + 1][1] - precision) and len(intervals) < 2:
            total = 0
            intervals.append(i)
        else:
            total += spam[i][1]

    print(intervals)
    div_spam.append(spam[:2])
    div_spam.append(spam[3:4])
    div_spam.append(spam[5:])
    return div_spam


def get_tree(string):
    string_count = Counter(string)
    prob = dict()
    for k, v in string_count.items():
        prob[k] = round((v / len(string)), 5)
    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}

    node = Node(None)

    length = 0
    spam = string_count.most_common()  # [('e', 2), ('s', 2), ('m', 1), ('a', 1), ('g', 1)]
    for s in spam:
        length += s[1]
    precision = length / TERNARY

    get_indexes(spam, precision)









    for i in range(len(spam) - 1):
        if abs(spam[i][1] - precision) < abs(spam[i][1] + spam[i + 1][1] - precision):
            ...




            #     if node.left is None:
            #         node.left = Node(spam[i])
            #         del string_count[spam[i][0]]
            #     elif node.mid is None:
            #         node.mid = Node(spam[i])
            #         del string_count[spam[i][0]]
            #     else:
            #         node.mid = Node(spam[i:])
            #         # del string_count[spam[i:][0]]
            # else:
            #     if node.left is None:
            #         node.left = Node(node.left spam[i])

        #
        # if isinstance(spam[0][0], str):
        #     node.left = Node(spam[0])
        # else:
        #     node.left = spam[0]
        #
        # if isinstance(spam[1][0], str):
        #     node.right = Node(spam[1])
        # else:
        #     node.right = spam[1]
        #
        # del string_count[spam[0]]
        # del string_count[spam[1]]
        # string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0], prob


def get_code(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes
    get_code(root.left, codes, code + '0')
    get_code(root.mid, codes, code + '1')
    get_code(root.right, codes, code + '2')
    return codes


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
