ALPHABET = {}
TERNARY = 3


def get_probability(string):
    string = string.strip()
    freq = {}
    prob = {}
    total = 0
    for s in string:
        if s not in freq.keys():
            freq[s] = 1
        else:
            freq[s] += 1
    for k, v in freq.items():
        prob[k] = v / len(string)
    for k, v in prob.items():
        total += v
    if total > 1.00001 or total < 0.99999:
        return False
    prob = {k: v for k, v in sorted(prob.items(), key=lambda item: item[1], reverse=True)}
    return prob


def get_leaf(probability, size):
    s = 0
    total = 0
    index = 0
    flag = True
    tree = {}
    leaf = {}
    interval = []
    for k, v in probability.items():
        total += v
    k = total / size

    for i, x in enumerate(probability.values()):
        if x:
            if abs(s - k) < abs(s + x - k) and len(interval) < 2:
                s = 0
                interval.append(i)
                if not leaf:
                    leaf[list(probability.keys())[i]] = list(probability.values())[i]
                    tree[index] = leaf.copy()
                    leaf.clear()
                    flag = False
                else:
                    tree[index] = leaf.copy()
                    leaf.clear()
                    leaf[list(probability.keys())[i]] = list(probability.values())[i]
                index += 1
                s += x
            else:
                leaf[list(probability.keys())[i]] = list(probability.values())[i]
                s += x
    else:
        if flag:
            tree[index] = leaf.copy()
    return tree


def get_tree(probability, size):
    origin_tree = get_leaf(probability, size)
    leaf = origin_tree.copy()
    for i in range(size):
        sub_tree = leaf.get(i)
        if sub_tree:
            while len(leaf.get(i)) > 1:
                sub_tree = get_tree(sub_tree, size)
                origin_tree[i].clear()
                origin_tree[i] = sub_tree
    return origin_tree


def get_coding(tree, code, result):
    for k, v in tree.items():
        new_code = code + str(k)
        if type(k) is str:
            new_code = new_code[:-1]
            char = k
            # result.append((new_code, char))
            ALPHABET[char] = new_code
        else:
            get_coding(v, new_code, result)


def encode(string):
    result = []
    code = ''
    encoded_string = ''
    prob = get_probability(string)
    tree = get_tree(prob, TERNARY)  # print("Probability Tree:", tree)
    get_coding(tree, code, result)
    for s in string:
        encoded_string += ALPHABET[s]
    print("Probability:", prob)
    print("Alphabet: ", ALPHABET)
    print("Encoding Result: ", encoded_string)


def main():
    string = input('Enter string: ')
    encode(string)


if __name__ == '__main__':
    main()
