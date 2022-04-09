import random


def extra_bits(length):
    return [i for i in range(1, length + 1) if not i & (i - 1)]


def insert_bits(data, bits):
    data = list(data)
    for bit in bits:
        data.insert(int(bit) - 1, "0")
    return "".join(d for d in data)


def calc_bits(source, bits):
    data = list(source)
    for bit in bits:
        i = bit - 1
        layout = ""
        counter = 0
        while i < len(data):
            for o in range(bit):
                if i + o < len(data):
                    counter += int(data[i + o])
                    layout += data[i + o]
            i += bit * 2
        data[bit - 1] = "1" if counter % 2 == 1 else "0"
    return ''.join(data)


def get_error(data):
    index = random.randint(0, len(data) - 1)
    return f'{data[:index]}_{1 - int(data[index])}_{data[index + 1:]}'


def find_error(source, bits):
    src = list(source)
    data = list(source)
    error_bits = []
    for bit in bits:
        i = bit - 1
        layout = ""
        counter = 0
        while i < len(data):
            for o in range(bit):
                if i + o < len(data):
                    counter += int(data[i + o])
                    layout += data[i + o]
            i += bit * 2
        if counter % 2 == 1 and counter % 2 != data[bit - 1]:
            error_bits.append(bit)
        data[bit - 1] = "1" if counter % 2 == 1 and counter % 2 != data[bit - 1] else "0"
    index = sum(error_bits) - 1
    bit = int(src[index])
    src[index] = str(1 - bit)
    return ''.join(src), error_bits


def get_blocks(data, size):
    return [f"{data[i:i + size]:<0{size}s}" for i in range(0, len(data), size)]


def bits2a(data, bits):
    data = list(data)
    for b in bits[::-1]:
        del data[b - 1]
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(data)]*8))


def main():
    size = 16  # Block size
    error_data = []
    source = input("Enter message: ")
    if len(source) % 2 == 1:
        source += ' '
    data = ''.join(format(ord(c), '08b') for c in source)
    data = get_blocks(data, size)
    print(f"{'Raw':<26}{'Parity Bits':<28}{'Determined bits':<28}")
    bits = extra_bits(size)
    for d in data:
        print(d, end=' ' * 10)
        d = insert_bits(d, bits)
        print(d, end=' ' * 7)
        d = calc_bits(d, bits)
        print(d, end='\n')
        error_data.append(d)
    print()
    print(f"{'Error Bit':<26}{'Bit index':<28}{'Raw Sequence':<25}")
    for d in error_data:
        d = get_error(d)
        print(d, end=' ' * 3)
        d = d.replace("_", "")
        src, error = find_error(d, bits)
        print(f"{str(error):<16} = {sum(error):>2}", end='')
        print(f"{src:>28}", end='   ')
        print(bits2a(src, bits))


if __name__ == '__main__':
    main()
