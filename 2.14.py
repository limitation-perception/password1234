def encode(string_val):
    c = 0
    encodedString = []

    if len(string_val) < 2:
        return (string_val, 1)

    for i in range(len(string_val) - 1):
        if string_val[i + 1] == string_val[i]:
            c += 1
        else:
            encodedString.append((string_val[i], c + 1))
            c = 0
    if c:
        encodedString.append((string_val[-1], c + 1))
    res = []
    for char in encodedString:
        res.append(char[0] + (str(char[1]) if char[1] > 1 else ''))
    return ''.join(res)


def decode(compressed_seq: str) -> str:
    seq = ""
    number = ""
    current_letter = None
    for character in compressed_seq:
        if character.isalpha():
            if current_letter is not None:
                seq += current_letter * int(number)

            current_letter = character
            number = ""
        else:
            number += character

    if current_letter is not None:
        seq += current_letter * int(number)

    return seq


if input() == 'C':
    s = input()
    enc = encode(s)
    print(enc if len(enc) < len(s) else s)
else:
    s = input()
    print(decode(s))
