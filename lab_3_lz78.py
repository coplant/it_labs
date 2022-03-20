def encode(message):
    encoded_str = ''
    dict_of_codes = {message[0]: '1'}
    encoded_str += '0' + message[0]
    message = message[1:]
    combination = ''
    code = 2
    for char in message:
        combination += char
        if combination not in dict_of_codes:
            dict_of_codes[combination] = str(code)
            if len(combination) == 1:
                encoded_str += '0' + combination
            else:
                encoded_str += dict_of_codes[combination[0:-1]] + combination[-1]
            code += 1
            combination = ''
    return encoded_str


def main():
    string = input('Enter string: ')
    result = encode(string)
    print(f'Encoding Result: {result}')


if __name__ == '__main__':
    main()
