from PIL import Image, ImageDraw
codes = {
    "0":
        {
            "A": "0001101", "B": "0100111", "C": "1110010",
        },
    "1":
        {
            "A": "0011001", "B": "0110011", "C": "1100110",
        },
    "2":
        {
            "A": "0010011", "B": "0011011", "C": "1101100",
        },
    "3":
        {
            "A": "0111101", "B": "0100001", "C": "1000010",
        },
    "4":
        {
            "A": "0100011", "B": "0011101", "C": "1011100",
        },
    "5":
        {
            "A": "0110001", "B": "0111001", "C": "1001110",
        },
    "6":
        {
            "A": "0101111", "B": "0000101", "C": "1010000",
        },
    "7":
        {
            "A": "0111011", "B": "0010001", "C": "1000100",
        },
    "8":
        {
            "A": "0110111", "B": "0001001", "C": "1001000",
        },
    "9":
        {
            "A": "0001011", "B": "0010111", "C": "1110100",
        }
}
parity = {
    "0": "AAAAAA",
    "1": "AABABB",
    "2": "AABBAB",
    "3": "AABBBA",
    "4": "ABAABB",
    "5": "ABBAAB",
    "6": "ABBBAA",
    "7": "ABABAB",
    "8": "ABABBA",
    "9": "ABBABA",
}


def get_control(number):
    sum_odd = sum([int(x) for i, x in enumerate(number) if i % 2 == 1])
    sum_even = sum([int(x) for i, x in enumerate(number) if i % 2 == 0])
    check_sum = sum_odd * 3 + sum_even
    control_number = (10 - (check_sum % 10)) % 10
    number = number + str(control_number)
    return number


def get_combination(number):
    c = "." + parity.get(number[0]) + "." + "C" * 6 + "."
    return c


def get_code(number, combination):
    code = ""
    number = list(number)
    number.insert(1, ".")
    number.insert(8, ".")
    number.insert(15, ".")
    for i, n in enumerate(number[1:]):
        if combination[i] != ".":
            code += codes[n][combination[i]]
        else:
            code += "."
    return code


def show_barcode(code):
    barcode = Image.new("RGB", (300, 150), "white")
    draw = ImageDraw.Draw(barcode)
    offset = 2.5
    start = 25
    i = 0
    for c in code:
        if c == "1":
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="black")
            i += 1
        elif c == "0":
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="white")
            i += 1
        elif c == ".":
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="white")
            i += 1
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="black")
            i += 1
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="white")
            i += 1
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="black")
            i += 1
            draw.rectangle((start + offset * i, 20, start + offset * i + offset, 130), fill="white")
            i += 1
    barcode.show()
    barcode.save("barcode.jpg")


def main():
    number = input("Enter SN [12]: ").replace(" ", '')
    while len(number) != 12 or not number.isdigit():
        print("Wrong SN! Try again..")
        number = input("Enter SN [12]: ")
    number = get_control(number)
    combination = get_combination(number)
    code = get_code(number, combination)
    show_barcode(code)


if __name__ == '__main__':
    main()
