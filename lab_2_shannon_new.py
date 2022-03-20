from collections import Counter


TERNARY = 3

class Node:
    def __init__(self, value, left=None, mid=None, right=None):
        self.right = right
        self.mid = mid
        self.left = left
        self.value = value


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



    #     # for i in range(len(string_count.values())):
    #     #     spam = list(string_count.keys())[i]
    #     #     print(spam)


    while len(string_count) != 0:
        node = Node(None)
        # [('e', 2), ('s', 2), ('m', 1), ('a', 1), ('g', 1)]
        spam = string_count.most_common()
        length = 0
        temp = []

        for s in spam:

            length += s[1]
        precision = length / TERNARY
        for i in range(len(spam) - 1):
            if isinstance(string_count[i], list) or abs(spam[i][1] - precision) < abs(spam[i][1] + spam[i + 1][1] - precision):
                if node.left is None:
                    if isinstance(spam[i][0], str):
                        node.left = Node(spam[i][0])
                    else:
                        node.left = spam[i][0]
                    del string_count[spam[i][0]]
                elif node.mid is None:
                    if isinstance(spam[i][0], str):
                        node.mid = Node(spam[i][0])
                    else:
                        node.mid = spam[i][0]
                    del string_count[spam[i][0]]
                else:
                    # while string_count != 1:
                    #     del string_count[spam[i][0]]
                    #     del string_count[spam[i + 1][0]]
                    #     string_count[node] = list(spam[i][1] + spam[i + 1][1])
                    #     i += 1
                    if len(string_count) == 1:
                        if isinstance(spam[i][0], list):
                            node.right = Node(spam[i][0])
                        else:
                            node.right = spam[i][0]
                        del string_count[spam[i][0]]
            else:
                del string_count[spam[i][0]]
                del string_count[spam[i + 1][0]]
                if spam[i] not in temp:
                    temp.append(spam[i])
                temp.append(spam[i + 1])
                string_count[node] = temp





        # spam = string_count.most_common()[:-3:-1]
        # if isinstance(spam[0][0], str):
        #     node.left = Node(spam[0][0])
        # else:
        #     node.left = spam[0][0]
        #
        # if isinstance(spam[1][0], str):
        #     node.right = Node(spam[1][0])
        #
        # else:
        #     node.right = spam[1][0]
        # del string_count[spam[0][0]]
        # del string_count[spam[1][0]]


    return [key for key in string_count][0], prob


def get_code(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes
    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')
    return codes


def coding(string, alpha):
    encoded_string = ''
    for char in string:
        encoded_string += alpha[char]
    return encoded_string


def encode(string):
    tree, prob = get_tree(string)
    # alpha = get_code(tree)
    # coding_str = coding(string, alpha)
    print(f'Probability: {prob}')
    # print(f'Alphabet: {alpha}')
    # print(f'Encoding Result: {coding_str}')


def main():
    string = input('Enter string: ')
    encode(string)


if __name__ == '__main__':
    main()