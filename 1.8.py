type_encryption = input()
shift_num = int(input())
words = input()
encrypted_char = ""
result = []
if type_encryption == "D":
    shift_num = - shift_num
for char in words:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord("a")
        encrypted_char = chr((ord(char) - start + shift_num) % 26 + start)
        result.append(encrypted_char)
    else:
        result.append(char)

print("".join(result))
